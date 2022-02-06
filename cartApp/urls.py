from django.urls import path
from . import views

# For easy access in the future to these routes
app_name = 'Cart'

urlpatterns = [
    
    path('add/<int:product_id>/', views.add_product, name='Add'),
    path('delete/<int:product_id>/', views.delete_product, name='Delete'),
    path('subtract/<int:product_id>/', views.subtract_product, name='Subtract'),
    path('clean/', views.clean_cart, name='Clean'),
]