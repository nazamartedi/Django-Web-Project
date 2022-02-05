from django.shortcuts import render
from .models import Product

def store(request):
    
     # Brings all the objcts created in that model
    products = Product.objects.all()
    
    return render(request, 'store/store.html', {'products':products})
