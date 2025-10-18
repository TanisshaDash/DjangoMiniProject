from django.shortcuts import render, redirect
from django.http import HttpResponse
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def home(request):
    return HttpResponse("<a href='/gmail/login/'>Login with Google</a>")


def gmail_login(request):
    """Step 1: Redirect user to Google's OAuth consent screen"""
    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": os.getenv("GOOGLE_CLIENT_ID"),
                "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
                "redirect_uris": [os.getenv("GOOGLE_REDIRECT_URI")],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
            }
        },
        scopes=SCOPES,
    )
    flow.redirect_uri = os.getenv("GOOGLE_REDIRECT_URI")

    authorization_url, state = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true",
        prompt="consent",
    )
    request.session["state"] = state
    return redirect(authorization_url)


def gmail_callback(request):
    """Step 2: Handle callback and exchange code for token"""
    state = request.session.get("state")

    if not state:
        return HttpResponse("Session expired. Try logging in again.")

    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": os.getenv("GOOGLE_CLIENT_ID"),
                "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
                "redirect_uris": [os.getenv("GOOGLE_REDIRECT_URI")],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
            }
        },
        scopes=SCOPES,
        state=state,
    )
    flow.redirect_uri = os.getenv("GOOGLE_REDIRECT_URI")

    # Google redirects user back with an auth code
    authorization_response = request.build_absolute_uri()
    flow.fetch_token(authorization_response=authorization_response)

    creds = flow.credentials
    request.session["credentials"] = {
        "token": creds.token,
        "refresh_token": creds.refresh_token,
        "token_uri": creds.token_uri,
        "client_id": creds.client_id,
        "client_secret": creds.client_secret,
        "scopes": creds.scopes,
    }
    return redirect("fetch_emails")


def fetch_emails(request):
    """Step 3: Fetch the user's latest emails"""
    creds_data = request.session.get("credentials")
    if not creds_data:
        return HttpResponse("No credentials found. Please log in first.")

    creds = Credentials(**creds_data)
    service = build("gmail", "v1", credentials=creds)

    results = service.users().messages().list(userId="me", maxResults=5).execute()
    messages = results.get("messages", [])

    email_data = []
    for msg in messages:
        m = service.users().messages().get(userId="me", id=msg["id"]).execute()
        headers = m["payload"].get("headers", [])
        subject = next((h["value"] for h in headers if h["name"] == "Subject"), "No Subject")
        sender = next((h["value"] for h in headers if h["name"] == "From"), "Unknown")
        snippet = m.get("snippet", "")
        email_data.append({"subject": subject, "sender": sender, "snippet": snippet})

    return render(request, "emails.html", {"emails": email_data})
