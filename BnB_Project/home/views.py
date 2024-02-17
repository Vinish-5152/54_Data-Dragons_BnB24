from django.contrib.auth.hashers import make_password, check_password
import json
from django.shortcuts import render, redirect
from .utils import *
from .forms import SignUpForm, LoginForm
from .models import *


# Create your views here.

def home(request):
    return render(request, 'Home.html')

def login(request):
    if request.method == 'GET':
        data = {
            'form': LoginForm
        }
        return render(request, 'Login.html', data)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']
            customer = Customer.objects.filter(Email=email).first()
            if customer:
                valid = check_password(password, customer.Password)
                if valid:
                    return redirect('HomePage')
                else:
                    form.add_error('Password', 'PASSWORD IS INCORRECT')
            else:
                form.add_error('Email', 'EMAIL DOES NOT EXISTS')
            return render(request, 'Login.html', {'form': form})
        else:
            data = {
                'form': form,
            }
            return render(request, 'Login.html', data)


def register(request):
    if request.method == 'GET':
        data = {
            'form': SignUpForm(),
        }
        return render(request, 'Register.html', data)

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            customer = form.save(commit=False)
            # Hash the password securely before saving
            customer.Password = make_password(form.cleaned_data['Password'])
            customer.Is_Email_Verified = True
            customer.Is_Phone_Number_Verified = True
            customer.save()
            try:
                del request.session['email_otp']
                del request.session['ph_number_otp']
            except KeyError:
                pass
            return redirect('HomePage')
        else:
            data = {
                'form': form,
            }
            return render(request, 'Register.html', data)


def register_otp_sender(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        if email:
            email_sender = Email_OTP()
            x = email_sender.send_otp_via_email(email)
            # Store the OTP in the session for later verification
            rst = json.loads(x.content.decode())
            if rst['status'] == 'success':
                request.session['email_otp'] = {email: email_sender.otp}
            return x
        else:
            return JsonResponse({'status': 'error', 'message': 'EMAIL PARAMETER IS MISSING'})
    else:
        return JsonResponse({'status': 'error', 'message': 'INVALID REQUEST METHOD'})


def register_otp_verifier(request):
    print('VERIFING')
    if request.method == 'GET':
        try:
            otp_data = request.session['email_otp']
        except KeyError:
            return JsonResponse({'status': 'error', 'message': 'KINDLY CLICK ON "Send Otp" FIRST'})
        email = request.GET.get('email')
        e_otp = request.GET.get('e_otp')
        print('Register otp verifier')
        email_verifier = Email_OTP()
        x = email_verifier.verify_otp_via_email(email, e_otp, otp_data)
        print(x)
        return x
    else:
        return JsonResponse({'status': 'error', 'message': 'INVALID REQUEST METHOD'})


def register_otp_sms_sender(request):
    if request.method == 'GET':
        ph_number = request.GET.get('ph')
        if ph_number:
            sms_sender = Phone_Number_OTP()
            x = sms_sender.send_otp_via_sms(ph_number)
            rst = json.loads(x.content.decode())
            if rst['status'] == 'success':
                request.session['ph_number_otp'] = {ph_number: sms_sender.otp}
            return x
        else:
            return JsonResponse({'status': 'error', 'message': 'PHONE NUMBER PARAMETER IS MISSING'})
    else:
        return JsonResponse({'status': 'error', 'message': 'INVALID REQUEST METHOD'})


def register_otp_sms_verifier(request):
    if request.method == 'GET':
        ph_number = request.GET.get('ph')
        e_otp = request.GET.get('e_otp')
        try:
            otp_data = request.session['ph_number_otp']
        except KeyError:
            return JsonResponse({'status': 'error', 'message': 'KINDLY CLICK ON "Send Otp" FIRST'})
        if ph_number and e_otp:
            print('OTP VERIFIER')
            sms_verifier = Phone_Number_OTP()
            x = sms_verifier.verify_otp_via_sms(ph_number, e_otp, otp_data)
            return x
        else:
            return JsonResponse({'status': 'error', 'message': 'PHONE NUMBER OR OTP PARAMETER IS MISSING'})
    else:
        return JsonResponse({'status': 'error', 'message': 'INVALID REQUEST METHOD'})
