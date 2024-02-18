from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Verifier_Profile)
class Verifier_Profile_Admin(admin.ModelAdmin):
    list_display = ['First_Name', 'Last_Name', 'Email', 'Is_Email_Verified', 'Phone_Number', 'Is_Phone_Number_Verified']