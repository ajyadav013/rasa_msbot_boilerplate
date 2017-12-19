import re
import os
import random

from app.models.user import (Users, OTP)
from app.middlewares.database import psql_db
from app.api.skype import SkypeAPI
from utils.mail import send_mail


class User(object):
    """
    Class to check user availablity
    instance as well as send OTP fro authentication and authenticate
    """

    def __init__(self):
        self.user_id = None
        self.user = None
        self.mail_sent = False
        self.user_registered = False
        self.otp_generated = False
        self.unregistered_user_mail_sent = False

    def registerUser(self, skypedata, replyObj):
        """
        Checks which scenario the user is
        currently in and send messages accordingly
        """
        print('Inside register user')
        if self.user_registered is False:
            print('Inside register user first if')
            if self.otp_generated is False:
                print('Inside register user second if')
                if self.unregistered_user_mail_sent is False:
                    print('Inside register user third if')
                    self.unregistered_user_mail_sent = True
                    replyObj.send_reply(  # Asking to provide email address
                        skypedata,
                        "I'm sorry but I can't find your email address, will you please provide your email address to authenticate?"
                    )
                else:
                    print('Inside register user first else')
                    # Received the email address, so validate it with
                    user_data = self.verifyUserEmail(skypedata, replyObj)
                    if user_data:
                        print('Inside register user first else first if')
                        # if true then generate otp and store it in db
                        if self.sendOTP(user_data, skypedata):
                            print('Inside register user first else second if')
                            self.otp_generated = True
                            replyObj.send_reply(skypedata, """OTP sent, Check your email and send the OTP here.  **Note- Validity of OTP is 10 minutes""")
                        else:
                            print('Inside register user second else')
                            replyObj.send_reply(skypedata,"""Oops...I think there are some issues while checking the OTP or sending the mail. Please contact System Admin. Thank You :)""")
                    else:  # Email not found
                        print('Inside register user third else')
                        # Sent the appropriate messages from verifyUserEmail method so just giving a pass here
                        pass
            else:  # Received the OTP, so validate it
                print('Inside register user fourth else')
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
            print('Inside checkORPexistance first try')
            user = Users.get(user_id=skypedata['from']['id'][3:])
            try:
                print('Inside checkORPexistance seconf try')
                OTP.get(user_id=user.id)
                replyObj.send_reply(skypedata, "Incorrect OTP, please send the correct one.")
            except OTP.DoesNotExist:
                print('Inside checkORPexistance first except')
                self.otp_generated = False
                self.user_registered = False
                replyObj.send_reply(skypedata, """I think you were off for a long time and the OTP would hav been expired. Can you please provide your email address?""")
        except Users.DoesNotExist:
            print('Inside checkORPexistance second except')
            self.user_registered = False
            self.otp_generated = False
            replyObj.send_reply(skypedata, """I think you were off for a long time or would have entered a wrong email address. Can you please provide your email address?""")

    def verifyOTP(self, skypedata):
        """
        Verify OTP with of specific user
        """
        try:
            print('Inside verifyOtp try')
            pattern = '[#!@$%]{{{}}}[\d]{{{}}}[!@#$%]{{{}}}'.format(os.environ.get('OTP_SPECIAL_CHARACTERS_LIMIT'), os.environ.get('OTP_DIGITS_LIMIT'), os.environ.get('OTP_SPECIAL_CHARACTERS_LIMIT'))
            # finds opt from the text entered by the user using regex
            otp = re.findall(pattern, skypedata['text'])
            if len(otp)==1 and (otp[0] in skypedata['text'].split()): # using split coz regex gives valid(matching regex) string from an invalid(valid regex but an incorrect otp) one too. it gives @#12345@# from string !@#12345@#$
                print('Inside verifyOtp first if')
                otp_obj = OTP.get(otp=otp[0])
                user = Users.get(id=otp_obj.user_id)
                if (user and user.user_id == skypedata['from']['id'][3:]):
                    print('Inside verifyOtp second if')
                    user.is_active = True
                    user.save()  # Make the user as active
                    return True
            return False
        except BaseException as e:
            print('Inside verifyOtp except')
            return False

    def verifyUserEmail(self, data, replyObj):
        """
        Verify Email
        """
        print('Inside verifyUserEmail')
        email = re.findall(r'[\w\.-]+@[\w\.-]+', data['text'])
        if email:
            print('Inside verifyUserEmail if')
            if len(set(email))==1: # The text comes in html format, so it amounts to 2 texts
                print('Inside verifyUserEmail second if')
                try:
                    print('Inside verifyUser try')
                    user_data = {"name":data['from']['name'], "email":email[0]}
                    return user_data
                except Exception as e:
                    replyObj.send_reply(data, """Please enter a correct one or contact System Admin. Thank You :)""")
            else:
                replyObj.send_reply(data, """I think you have entered multiple email addresses. Can you please enter a correct one?""")
        else:
            replyObj.send_reply(data, """I think you have entered an invalid email address. Can you please send a valid one?""")
        return False

    def sendOTP(self, user_data, skypedata):
        """
        Sends OTP, based in the number of digits set in environment
        """
        try:
            print('Inside sendOTP try')
            digits = int(os.environ.get('OTP_DIGITS_LIMIT'))
            otp_special_char = os.environ.get('OTP_SPECIAL_CHARACTERS')
            otp = ''.join(random.sample(otp_special_char, 2)) + str(random.randint(10**(digits - 1), 10**digits)) + ''.join(random.sample(otp_special_char, 2))
            if self.createUserOTP(user_data, skypedata, otp):
                if send_mail(user_data['email'], user_data['name'], otp):
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
            print('Inside createOTP')
            user = Users.get_or_create(
                name=user_data['name'],
                user_id=skypedata['from']['id'][3:],
                is_active=False)
            try:
                otp_obj = OTP.get(user_id=user[0].id)
                otp_obj.otp = otp
                otp_obj.save()
            except OTP.DoesNotExist:
                OTP.create(user_id=user[0].id, otp=otp)
            return True
        except Exception as e:
            print('CreateUser OTP exception', e)
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
                print('message data', message_data)
                user = Users.get(user_id=message_data['from']['id'][3:])
                print('User', user)
                if user.is_active is True:
                    message_data['user'] = user
                else:
                    self.registerUser(message_data, reply)
                    message_data['user'] = None
            except BaseException:
                print('Inside user except')
                self.registerUser(message_data, reply)
                message_data['user'] = None
                req.context['request'] = message_data

        except BaseException:
            print('Inside user base exception')
            req.context['request'] = {}

    def process_response(self, req, resp, resource, request_succeded):
        """
        Middleware Response
        """
        pass
