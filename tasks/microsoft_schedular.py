import requests
import json
import os
import datetime
from app.models.authentication import MicrosoftAuthentication

def refreshMicrosoftToken(microsoft_client_id=None, microsoft_client_secret=None):
    """
        Return microsoft bot framework connection token.
    """
    try:
        bot_data = 'grant_type=client_credentials&client_id=' + microsoft_client_id + '&client_secret=' + \
            microsoft_client_secret + '&scope=https%3A%2F%2Fapi.botframework.com%2F.default'
        token = requests.post(
            """https://login.microsoftonline.com/botframework.com/oauth2/v2.0/token""",
            data=bot_data,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        )
        return json.loads(token.text)

    except Exception as e:
        print("Exception in tokenn microsoft token ", e)

if __name__ == '__main__':
    microsoft_client_id = os.environ.get('MICROSOFT_CLIENT_ID')
    microsoft_client_secret = os.environ.get('MICROSOFT_CSE_ID')
    microsoft_refresh_seconds = float(os.environ.get('MICROSOFT_TOKEN_REFRESH_SECONDS'))
    try:
        record = MicrosoftAuthentication.select().limit(1)[0]
    except:
        record = None
    if (record == None):
        token = refreshMicrosoftToken(microsoft_client_id, microsoft_client_secret)
        MicrosoftAuthentication.create(token=token['access_token'])
    elif (record.refresh_time + \
            datetime.timedelta(seconds=microsoft_refresh_seconds) <= \
            datetime.datetime.now()):
        record.token = refreshMicrosoftToken(microsoft_client_id, microsoft_client_secret)['access_token']
        record.refresh_time = datetime.datetime.now()
        record.save()

