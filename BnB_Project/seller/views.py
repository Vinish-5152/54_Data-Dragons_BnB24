from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, 'Seller_Home.html')

def product(request):
    return render(request,'Seller_Product.html')

def add_product(request):
    if request.method == 'GET':
        data = {
            'form': AddProductForm(),
        }
        return render(request, 'Seller_Product.html', data)

    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            pass

    '''p_category = Category.objects.all()
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
'''