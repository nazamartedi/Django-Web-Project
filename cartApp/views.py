from django.shortcuts import render, redirect
from .cart import Cart
from storeApp.models import Product

def add_product(request, product_id):
    
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    
    # url name given in urls.py
    return redirect('Store') 

def delete_product(request, product_id):
    
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.delete(product=product)
    
    # url name given in urls.py
    return redirect('Store')

def subtract_product(request, product_id):
    
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.subtract_product(product=product)
    
    # url name given in urls.py
    return redirect('Store')

def clean_cart(request):
    
    cart = Cart(request)
    cart.clean_cart()
    
    # url name given in urls.py
    return redirect('Store')   