#Standard library imports
from os import path

#Third party imports
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

def authenticate(tokenfile, scopes):
    """
    Performs oauth following the installed application flow
    -------------------------------------------------------

    arguments:
        - tokenfile: file name containing oauth token in json format,
        gets created automatically when the flow completes first time
        - scopes: list of scopes                    
    """

    creds = None
    if path.exists(tokenfile):
        creds = Credentials.from_authorized_user_file(tokenfile, scopes)
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
        return creds
    
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_credentials.json', scopes
        )
        creds = flow.run_local_server()
        with open(tokenfile, 'x') as tf:
            tf.write(creds.to_json())
        return creds    

