"""
Fetch he access token and refresh token based on their time intervals specified
"""
import requests
import json
import os
import datetime
from app.models.authentication import Authentication

def makeAPICall(*args, username=None, password=None, **kwargs):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    auth_record = args[0]
    data = {
        'grant_type': kwargs['grant_type'],
        'client_id': os.environ.get('SERVICENOW_OAUTH_CLIENT_ID'),
        'client_secret': os.environ.get('SERVICENOW_OAUTH_CLIENT_SECRET'),
        'refresh_token': auth_record.refresh_token,
        'username': username,
        'password': password,
    }
    response = requests.post(os.environ.get(
        'SERVICENOW_OAUTH_BASE_URL'), headers=headers, data=data)
    response = json.loads(response.text)
    try:
        if kwargs['grant_type'] == 'password':
            auth_record.refresh_token = response['refresh_token']
            auth_record.refresh_expiry = datetime.datetime.now()
        else:
            auth_record.access_token = response['access_token']
            auth_record.access_expiry = datetime.datetime.now()
        auth_record.save()
    except Exception as e:
        print('Exception in tokenn-', e)

if __name__ == '__main__':
    auth_record = [i for i in Authentication.select().limit(1)][0]
    refresh_expiry = (
        auth_record.refresh_expiry +
        datetime.timedelta(
            seconds=int(
                os.environ.get(
                    'SERVICENOW_REFRESH_TOKEN_EXPIRY'
                )
            )
        )
    ) - datetime.datetime.now()
    access_expiry = (
        auth_record.access_expiry +
        datetime.timedelta(
            seconds=int(
                os.environ.get(
                    'SERVICENOW_ACCESS_TOKEN_EXPIRY'
                )
            )
        )
    ) - datetime.datetime.now()
    if refresh_expiry.total_seconds() <= 0:
        makeAPICall(
            auth_record,
            username=os.environ.get('SERVICENOW_INSTANCE_USERNAME'),
            password=os.environ.get('SERVICENOW_INSTANCE_PASSWORD'),
            grant_type='password'
        )
    if access_expiry.total_seconds() <= 0:
        makeAPICall(auth_record, grant_type='refresh_token')
