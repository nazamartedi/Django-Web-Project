from django.shortcuts import render
from servicesApp.models import Services

def services(request):
    
    # Brings all the objcts created in that model
    services = Services.objects.all()
     
    return render(request, 'services/services.html', {'services':services})