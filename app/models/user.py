from datetime import datetime
from .abs import ABS
import peewee

class Users(ABS):
    """
    Model to store Users Data
    """
    name = peewee.CharField(max_length=100)
    user_id = peewee.CharField(max_length=200, unique=True)
    servicenow_id = peewee.CharField(max_length=200, unique=True)
    is_active = peewee.BooleanField()

class OTP(ABS):
    """
    Model to OTP of specific user
    """
    user = peewee.ForeignKeyField(Users)
    otp = peewee.CharField(max_length=10)
    set_time = peewee.DateTimeField(default=datetime.now)
