from django.shortcuts import render

def home(request):
    
    return render(request, 'home.html')


# def services(request):
    
#     # Brings all the objcts created in that model
#     services = Services.objects.all()
     
#     return render(request, 'services.html', {'services':services})


def store(request):
    
    return render(request, 'store.html')


# def blog(request):
    
#     return render(request, 'blog.html')


# def contact(request):
    
#     return render(request, 'contact.html')
