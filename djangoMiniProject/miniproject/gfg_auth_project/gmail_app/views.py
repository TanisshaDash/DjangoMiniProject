from django.shortcuts import render, redirect
from django.http import HttpResponse
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from django.conf import settings

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def home(request):
    return HttpResponse("<a href='/gmail/login/'>Login with Google</a>")

def gmail_login(request):
    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": settings.GOOGLE_CLIENT_ID,
                "client_secret": settings.GOOGLE_CLIENT_SECRET,
                "redirect_uris": [settings.GOOGLE_REDIRECT_URI],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs"
            }
        },
        scopes=SCOPES,
        redirect_uri=settings.GOOGLE_REDIRECT_URI
    )
    auth_url, state = flow.authorization_url(access_type='offline', prompt='consent')
    request.session['state'] = state
    return redirect(auth_url)

def gmail_callback(request):
    state = request.session.get('state')
    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": settings.GOOGLE_CLIENT_ID,
                "client_secret": settings.GOOGLE_CLIENT_SECRET,
                "redirect_uris": [settings.GOOGLE_REDIRECT_URI],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs"
            }
        },
        scopes=SCOPES,
        state=state,
        redirect_uri=settings.GOOGLE_REDIRECT_URI
    )
    flow.fetch_token(authorization_response=request.build_absolute_uri())
    creds = flow.credentials
    request.session['credentials'] = {
        'token': creds.token,
        'refresh_token': creds.refresh_token,
        'token_uri': creds.token_uri,
        'client_id': creds.client_id,
        'client_secret': creds.client_secret,
        'scopes': creds.scopes
    }
    return redirect('fetch_emails')

def fetch_emails(request):
    creds_data = request.session.get('credentials')
    if not creds_data:
        return HttpResponse("No credentials. Login first.")
    creds = Credentials(**creds_data)
    service = build('gmail', 'v1', credentials=creds)
    result = service.users().messages().list(userId='me', maxResults=5).execute()
    messages = result.get('messages', [])
    email_data = []
    for msg in messages:
        m = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = m['payload'].get('headers', [])
        subject = next((h['value'] for h in headers if h['name']=='Subject'), 'No Subject')
        sender = next((h['value'] for h in headers if h['name']=='From'), 'Unknown')
        snippet = m.get('snippet', '')
        email_data.append({'subject': subject, 'sender': sender, 'snippet': snippet})
    return render(request, 'emails.html', {'emails': email_data})
