import smtplib
import os
import email.message


def send_mail(recepient_email, name, otp):
    msg = email.message.Message()
    msg['Subject'] = "User Verification"
    msg['From'] = os.environ.get('EMAIL_HOST')
    msg['To'] = recepient_email
    msg.add_header('Content-Type', 'text/html')
    text = """\
    <html style="margin:0px; padding:0px">
        <body style="margin:0px; padding:0px; ">
            <div style="margin:0px 8px; font-family:Times; font-color:black; text-align: justify;">
                <p style='font-size:16px !important;'>Hi {},</p>
                <div>
                    <div>
                        <p style='font-size:16px !important;'>Please enter this OTP - <strong>{}</strong> in the chat window in order to authenticate yourself.</p>
                    </div>
                    <div>
                        Please Note -
                        <ul style='font-size:16px !important;'>
                            If you did <strong>not</strong> request the OTP, please <strong>contact us</strong> so we can investigate it further.
                        </ul>
                    </div>
                </div>
                <div style="margin-top:10px; font-size:16px;">
                    Regards, <br/>
                    https://github.com/ajyadav013
                </div>
            </div>
         </body>
    </html>
    """.format(name, otp)
    msg.set_payload(text)
    try:
        server = smtplib.SMTP('smtp.gmail.com')
        server.starttls()
        server.login(os.environ.get('EMAIL_HOST'),
                     os.environ.get('EMAIL_HOST_PASSWORD'))
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print('Mail exception', e)
        return False
