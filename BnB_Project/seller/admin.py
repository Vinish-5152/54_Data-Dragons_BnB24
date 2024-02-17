from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Seller_Profile)
class SellerProfileAdmin(admin.ModelAdmin):
    list_display = ['First_Name', 'Last_Name', 'Email', 'Is_Email_Verified', 'Phone_Number', 'Is_Phone_Number_Verified']
    search_fields = ['First_Name', 'Last_Name', 'Email', 'Phone_Number']
    list_filter = ['Is_Email_Verified', 'Is_Phone_Number_Verified']
    list_per_page = 10
    list_editable = ['Is_Email_Verified', 'Is_Phone_Number_Verified']
    actions = ['make_email_verified', 'make_phone_verified']