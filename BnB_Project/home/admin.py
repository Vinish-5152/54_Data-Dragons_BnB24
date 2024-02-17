from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name', 'Email', 'Phone_Number')
    search_fields = ['Email', 'Phone_Number']
    pass