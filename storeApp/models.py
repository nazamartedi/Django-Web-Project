from distutils.command.upload import upload
from tabnanny import verbose
from tkinter import CASCADE
from unicodedata import category
from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'prodCategory'
        verbose_name_plural = 'prodCategories' 

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    categories = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store', null=True, blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products' 

    
