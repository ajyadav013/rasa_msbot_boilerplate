"""
Check if the OTP has passed 10 minutes
after being created and if True
then delete that record
"""
import os
import datetime
from app.models.user import OTP

expiry_time = datetime.datetime.now(
) - datetime.timedelta(minutes=int(os.environ.get('OTP_LIFETIME')))
query = OTP.delete().where(expiry_time < OTP.set_time)
query.execute()
