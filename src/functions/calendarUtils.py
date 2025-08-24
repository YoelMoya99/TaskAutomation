from __future__ import print_function
import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Full access to read/write calendar
SCOPES = ['https://www.googleapis.com/auth/calendar']

def calendarSetUp():
    varCreds = None
    
    # Load the existing token if present...
    if os.path.exists('../creds/token.json'):
        varCreds = Credentials.from_authorized_user_file('../creds/token.json', SCOPES)

    # If no valid token, do login
    if not varCreds or not varCreds.valid:
        if varCreds and varCreds.expired and varCreds.refresh_token:
            varCreds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '../creds/credentials.json', SCOPES)
            varCreds = flow.run_local_server(port=0)
        with open('../creds/token.json', 'w') as token:
            token.write(varCreds.to_json())

    service = build('calendar', 'v3', credentials=varCreds)
    return service
