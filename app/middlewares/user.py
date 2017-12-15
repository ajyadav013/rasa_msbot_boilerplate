import re
import os
import random

from app.models.user import (Users, OTP)
from app.middlewares.database import psql_db
from app.api.skype import SkypeAPI
from servicenow.api import ServiceNow
from utils.mail import send_mail


class User(object):
    """
    Class to check user availablity in servicenow
    instance as well as send OTP fro authentication and authenticate
    """

    def __init__(self):
        self.user_id = None
        self.user = None
        self.mail_sent = False
        self.user_registered = False
        self.otp_generated = False
        self.unregistered_user_mail_sent = False
        self.service = ServiceNow()

    def registerUser(self, skypedata, replyObj):
        """
        Checks which scenario the user is
        currently in and send messages accordingly
        """
        if self.user_registered is False:
            if self.otp_generated is False:
                if self.unregistered_user_mail_sent is False:
                    self.unregistered_user_mail_sent = True
                    replyObj.send_reply(  # Asking to provide email address
                        skypedata,
                        self.service.all_errors['unregistered_user']
                    )
                else:
                    # Received the email address, so validate it with
                    # servicenow instance
                    user_data = self.verifyServiceNowUserEmail(skypedata, replyObj)
                    if user_data:
                        # if true then generate otp and store it in db
                        if self.sendOTP(user_data, skypedata):
                            self.otp_generated = True
                            replyObj.send_reply(skypedata, """OTP sent, Check your email and send the OTP here.  **Note- Validity of OTP is 10 minutes""")
                        else:
                            replyObj.send_reply(skypedata,"""Oops...I think there are some issues while checking the OTP. Please contact System Admin. Thank You :)""")
                    else:  # Email not found in servicenow instance
                        # Sent the appropriate messages from verifyServiceNowUserEmail method so just giving a pass here
                        pass
            else:  # Received the OTP, so validate it
                if self.verifyOTP(skypedata):
                    replyObj.send_reply(
                        skypedata,
                        "Authentication successful, How can I help you?")
                else:
                    # check if otp has expired. If expired then start the whole process again else just ask to send proper otp
                    self.checkOTPExistance(skypedata, replyObj)
                    
    def checkOTPExistance(self, skypedata, replyObj):
        """
        Check if OTP already exists for the specific email address
        """
        try:
            user = Users.get(user_id=skypedata['from']['id'][3:])
            try:
                OTP.get(user_id=user.id)
                replyObj.send_reply(skypedata, "Incorrect OTP, please send the correct one.")
                #return True
            except OTP.DoesNotExist:
                self.otp_generated = False
                self.user_registered = False
                replyObj.send_reply(skypedata, """I think you were off for a long time and the OTP would hav been expired. Can you please provide your servicenow registered email address?""")
                #return False
        except Users.DoesNotExist:
            self.user_registered = False
            self.otp_generated = False
            replyObj.send_reply(skypedata, """I think you were off for a long time or would have entered a wrong email address. Can you please provide your servicenow registered email address?""")
            #return False

    def verifyOTP(self, skypedata):
        """
        Verify OTP with of specific user
        """
        try:
            pattern = '[#!@$%]{{{}}}[\d]{{{}}}[!@#$%]{{{}}}'.format(os.environ.get('OTP_SPECIAL_CHARACTERS_LIMIT'), os.environ.get('OTP_DIGITS_LIMIT'), os.environ.get('OTP_SPECIAL_CHARACTERS_LIMIT'))
            # finds opt from the text entered by the user using regex
            otp = re.findall(pattern, skypedata['text'])
            #otp = re.findall(r'FUJIAMAZE+[\d]+', skypedata['text'])
            if len(otp)==1 and (otp[0] in skypedata['text'].split()): # using split coz regex gives valid(matching regex) string from an invalid(valid regex but an incorrect otp) one too. it gives @#12345@# from string !@#12345@#$
                otp_obj = OTP.get(otp=otp[0])
                user = Users.get(id=otp_obj.user_id)
                if (user and user.user_id == skypedata['from']['id'][3:]):
                    user.is_active = True
                    user.save()  # Make the user as active
                    return True
            return False
        except BaseException as e:
            return False

    def verifyServiceNowUserEmail(self, data, replyObj):
        """
        Verify Email with Servicenow instance mail id
        """
        email = re.findall(r'[\w\.-]+@[\w\.-]+', data['text'])
        if email:
            if len(set(email))==1: # The text comes in html format, so it amounts to 2 texts
                try:
                    user_data = self.service.getData('user', email=email[0])
                    return user_data['result'][0]
                except BaseException:
                    replyObj.send_reply(data, """I'm sorry, your email address doesn't exist in the service now instance. Please enter a correct one or contact System Admin. Thank You :)""")
            else:
                replyObj.send_reply(data, """I think you have entered multiple email addresses. Can you please enter a correct one which corresponds with your servicenow account?""")
        else:
            replyObj.send_reply(data, """I think you have entered an invalid email address. Can you please send a valid one?""")
        return False

    def sendOTP(self, user_data, skypedata):
        """
        Sends OTP, based in the number of digits set in environment
        """
        try:
            digits = int(os.environ.get('OTP_DIGITS_LIMIT'))
            otp_special_char = os.environ.get('OTP_SPECIAL_CHARACTERS')
            otp = ''.join(random.sample(otp_special_char, 2)) + str(random.randint(10**(digits - 1), 10**digits)) + ''.join(random.sample(otp_special_char, 2))
            if self.createUserOTP(user_data, skypedata, otp):
                send_mail(user_data['email'], user_data['name'], otp)
                return True
            return False
        except Exception as e:
            print('send OTP except', e)

    @psql_db.atomic()
    def createUserOTP(self, user_data, skypedata, otp):
        """
        Creates or fetches User and OTP atomically
        """
        try:
            user = Users.get_or_create(
                name=user_data['name'],
                user_id=skypedata['from']['id'][3:],
                servicenow_id=user_data['sys_id'],
                is_active=False)
            try:
                otp_obj = OTP.get(user_id=user[0].id)
                otp_obj.otp = otp
                otp_obj.save()
            except OTP.DoesNotExist:
                OTP.create(user_id=user[0].id, otp=otp)
            return True
        except Exception as e:
            return False


class UserMiddleware(User):
    """
    Middleware for checking user authenticity
    """

    def __init__(self):
        super().__init__()

    def process_resource(self, req, resp, resource, params):
        """
        Middleware Request
        """
        try:
            message_data = req.context['request']
            reply = SkypeAPI()
            try:
                user = Users.get(user_id=message_data['from']['id'][3:])
                if user.is_active is True:
                    message_data['user'] = user
                else:
                    self.registerUser(message_data, reply)
                    message_data['user'] = None
            except BaseException:
                self.registerUser(message_data, reply)
                message_data['user'] = None
                req.context['request'] = message_data

        except BaseException:
            req.context['request'] = {}

    def process_response(self, req, resp, resource, request_succeded):
        """
        Middleware Response
        """
        pass
