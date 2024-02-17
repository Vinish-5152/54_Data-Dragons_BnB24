"""
URL configuration for BnB_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="Home_HomePage"),
    path('login/', login, name='Home_LoginPage'),
    path('register/', register, name='Home_RegisterPage'),
        path('register/send_otp_via_email/', register_otp_sender, name='send_otp_via_email'),
    path('register/verify_otp_via_email/', register_otp_verifier, name='verify_otp_via_email'),
    path('register/send_otp_via_sms/', register_otp_sms_sender, name='send_otp_via_sms'),
    path('register/verify_otp_via_sms/', register_otp_sms_verifier, name='verify_otp_via_sms'),
    path('user/', userchoice, name='UserPage'),
    path('logout/', logout, name='LogoutPage'),
]
