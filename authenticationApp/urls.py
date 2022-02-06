from django.urls import path
from .views import VAuth

urlpatterns = [
   path('', VAuth.as_view(), name='Authentication'),
]