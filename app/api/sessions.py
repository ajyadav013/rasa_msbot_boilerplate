import json
import requests
import os
from app.models.authentication import MicrosoftAuthentication
from tasks.microsoft_schedular import refreshMicrosoftToken

def microsoft_bot_framework_connect():
    """
        Return microsoft bot framework connection token.
    """
    try:
        record = MicrosoftAuthentication.select().limit(1)
        return record[0].token
    except Exception as e:
        microsoft_client_id = os.environ.get('MICROSOFT_CLIENT_ID')
        microsoft_client_secret = os.environ.get('MICROSOFT_CSE_ID')
        record = refreshMicrosoftToken(microsoft_client_id, microsoft_client_secret)
        return record['access_token']
