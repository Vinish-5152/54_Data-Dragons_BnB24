from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name='Seller_HomePage'),
    path('product/',product,name='Seller_product'),
    path('product/add_product/',add_product,name='Seller_add_product'),
]
