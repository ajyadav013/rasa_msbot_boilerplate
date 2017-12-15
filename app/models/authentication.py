from datetime import datetime
from .abs import ABS
import peewee

class Authentication(ABS):
    """
    Authentication class to store appropriate access, refresh tokens
    """
    access_token = peewee.CharField(max_length=200, unique=True)
    refresh_token = peewee.CharField(max_length=200, unique=True)
    access_expiry = peewee.DateTimeField(default=datetime.now)
    refresh_expiry = peewee.DateTimeField(default=datetime.now)

class MicrosoftAuthentication(ABS):
    '''
        Microsoft bot framework token model
    '''

    token = peewee.CharField(max_length=1500)
    refresh_time = peewee.DateTimeField(default=datetime.now)
