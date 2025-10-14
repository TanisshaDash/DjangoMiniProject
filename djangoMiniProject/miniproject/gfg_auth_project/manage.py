import os
import sys
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from django.conf import settings

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def home(request):
    return HttpResponse("<a href='/gmail/login/'>Login with Google</a>")

# rest of your gmail_login, gmail_callback, fetch_emails functions...


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gfg_auth_project.settings')
  
    load_dotenv()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
