from django.contrib.auth.hashers import make_password, check_password
import json
from django.shortcuts import render, redirect
from .utils import *
from .forms import SignUpForm, LoginForm
from .models import *
from seller.models import Seller_Profile
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def home(request):
    data = {
        'customer_id': request.session.get('customer_id'),
    }

    return render(request, 'Home.html', {'data': data})

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
                    request.session['customer_id'] = customer.id
                    return redirect('UserPage')
                else:
                    form.add_error('Password', 'PASSWORD IS INCORRECT')
            else:
                form.add_error('Email', 'EMAIL DOES NOT EXISTS')
            return render(request, 'Login.html', {'form': form})
        useremail=request.POST['Email']
        userpassword=request.POST['Password']
        myuser=authenticate(request,email=useremail, password=userpassword)
        print(myuser)
        print(useremail,userpassword)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Success")
            return redirect('/home')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/logi')
    return render(request, "Login.html")
    #     if form.is_valid():
    #         email = form.cleaned_data['Email']
    #         password = form.cleaned_data['Password']
    #         customer = Customer.objects.filter(Email=email).first()
    #         if customer:
    #             valid = check_password(password, customer.Password)
    #             if valid:
    #                 return redirect('HomePage')
    #             else:
    #                 form.add_error('Password', 'PASSWORD IS INCORRECT')
    #         else:
    #             form.add_error('Email', 'EMAIL DOES NOT EXISTS')
    #         return render(request, 'Login.html', {'form': form})
    #     else:
    #         data = {
    #             'form': form,
    #         }
    #         return render(request, 'Login.html', data)

    
    # if request.method=="POST":
    #     username=request.POST['Email']
    #     userpassword=request.POST['pass1']
    #     myuser=authenticate(username=username, password=userpassword)
    #     if myuser is not None:
    #         login(request, myuser)
    #         messages.success(request, "Login Success")
    #         return redirect('/')
    #     else:
    #         messages.error(request, "Invalid Credentials")
    #         return redirect('/auth/login')
    # return render(request, "authentication/login.html")

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
            return redirect('LoginPage')
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

def logout(request):
    try:
        del request.session
    except KeyError:
        pass
    return redirect('Home_HomePage')

def userchoice(request):
    if request.method == 'GET':
        return render(request, 'Verified_User.html')
    if request.method == 'POST':
        print("FORM SUBMITTED")
        user_type = request.GET.get('user_type')
        print(user_type)
        customer = Customer.objects.get(pk=request.session.get('customer_id'))
        if user_type == 'seller':
            new_seller = Seller_Profile(First_Name=customer.First_Name, Last_Name=customer.Last_Name, Email=customer.Email, Is_Email_Verified=customer.Is_Email_Verified, Phone_Number=customer.Phone_Number, Is_Phone_Number_Verified=customer.Is_Phone_Number_Verified, Password=customer.Password)
            #new_seller.save()
            print('SAVED')
            request.session['seller_id'] = new_seller.id
            del request.session['customer_id']
            return JsonResponse({'status': 'success', 'message': 'REDIRECTING TO SELLER PAGE'})
    return render(request, 'Verified_User.html')



def handlelogin(request):
    if request.method=="POST":
        username=request.POST['Email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username, password=userpassword)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Success")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/auth/login')
    return render(request, "authentication/login.html")


def handlelogout(request):
    logout(request)
    messages.info(request,'Logout Success')
    return redirect("/auth/login")
