import smtplib
import string
import random
import requests
from django.conf import settings
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse


class Email_OTP:
    def __init__(self):
        self.otp = None

    def generate_otp(self, length=6):
        characters = string.digits
        self.otp = ''.join(random.choice(characters) for _ in range(length))

    def send_otp_via_email(self, email):
        print(email)
        print('OTP CALLED')
        if email:
            # Use self._generate_otp instead of _generate_otp
            self.generate_otp()
            print(self.otp)
            subject = 'Hoop-Art: Your Otp Verification Code'
            message = f'''
Your Otp Verification: {self.otp}
'''
            email_from = settings.EMAIL_HOST_USER
            try:
                x = send_mail(subject, message, email_from, [email], fail_silently=False)
            except ValueError:
                return JsonResponse({'status': 'error', 'message': "CAN'T SEND OTP TO THIS EMAIL ID"})
            except smtplib.SMTPRecipientsRefused:
                return JsonResponse({'status': 'error', 'message': "CAN'T SEND OTP TO THIS EMAIL ID"})
            if x == 1:
                print('Otp Sent Successfully!...')
                return JsonResponse({'status': 'success', 'message': 'OTP SENT SUCCESSFULLY'})
            else:
                print('Error sending OTP...')
                return JsonResponse({'status': 'error', 'message': 'ERROR SENDING OTP'})
        else:
            return JsonResponse({'status': 'error', 'message': 'EMAIL PARAMETER IS MISSING'})

    def verify_otp_via_email(self, email, e_otp, otp_data):
        print('verify otp via email')
        try:
            s_otp = otp_data[email]
        except KeyError:
            return JsonResponse({'status': 'error', 'message': f'OTP VERIFICATION FAILED'})
        if e_otp is not None:
            if s_otp is not None:

                if len(s_otp) != len(e_otp):
                    print('INVALID OTP')
                    return JsonResponse({'status': 'error', 'message': 'INVALID OTP'})
                if int(s_otp) == int(e_otp):
                    print('VERIFIED')
                    return JsonResponse({'status': 'success', 'message': 'OTP VERIFIED'})
                else:
                    print('INVALID OTP 2')
                    return JsonResponse({'status': 'error', 'message': 'INVALID OTP'})
            else:
                print('ENTER A VALID OTP')
                return JsonResponse({'status': 'error', 'message': 'ENTER A VALID OTP'})
        else:
            print('KINDLY CLICK ON OTP')
            return JsonResponse({'status': 'error', 'message': 'KINDLY CLICK ON "Send Otp" FIRST'})


class Phone_Number_OTP:
    def __init__(self):
        self.otp = None
        self.__api = settings.SMS_TOKEN

    def generate_otp(self, length=6):
        characters = string.digits
        self.otp = ''.join(random.choice(characters) for _ in range(length))

    def send_otp_via_sms(self, phone_number):
        self.generate_otp()
        url = f'https://2factor.in/API/V1/{self.__api}/SMS/+91{phone_number}/{self.otp}/Hoop-Art'
        response = requests.get(url)
        data = response.json()

        print(data)
        if data['Status'] == 'Success':
            return JsonResponse({'status': 'success', 'message': 'OTP SENT SUCCESSFULLY'})
        else:
            return JsonResponse({'status': 'error', 'message': "CAN'T SEND OTP, TRY AGAIN LATER"})

    def verify_otp_via_sms(self, phone_number, e_otp, otp_data):
        print('Verifying OTP')
        try:
            s_otp = otp_data[phone_number]
        except KeyError:
            return JsonResponse({'status': 'error', 'message': 'OTP VERIFICATION FAILED'})
        if e_otp is not None:
            if s_otp is not None:
                if len(s_otp) != len(e_otp):
                    print('INVALID OTP')
                    return JsonResponse({'status': 'error', 'message': 'INVALID OTP'})
                if int(s_otp) == int(e_otp):
                    print('VERIFIED')
                    return JsonResponse({'status': 'success', 'message': 'OTP VERIFIED'})
                else:
                    print('INVALID OTP 2')
                    return JsonResponse({'status': 'error', 'message': 'INVALID OTP'})
            else:
                print('ENTER A VALID OTP')
                return JsonResponse({'status': 'error', 'message': 'ENTER A VALID OTP'})
        else:
            print('KINDLY CLICK ON OTP')
            return JsonResponse({'status': 'error', 'message': 'KINDLY CLICK ON "Send Otp" FIRST'})
