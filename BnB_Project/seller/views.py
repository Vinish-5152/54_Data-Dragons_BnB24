from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.

def home(request):
    return render(request, 'Seller_Home.html')

def product(request):
    return render(request,'Product.html')

def add_product(request):
    p_category = Category.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        # category = Category.objects.get(id = request.POST['category'])
        price = request.POST['price']
        quantity = request.POST['quantity']
        description = request.POST['desc']


        data = Product(
            Name=name,
            Price=price,
            Quantity=quantity,
            Description=description,
            # category=category
            )
        data.save()


        return redirect('/seller/product')
    else:
        form = add_product(request)

    return render(request, 'product/add_product.html', {'form': form, 'p_category':p_category})
