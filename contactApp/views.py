from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    
    # We need to instantiate a ContactForm object in order to show it on the template
    contact_form = ContactForm()
    
    # Getting all the info from the form
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')
            
            # If success
            return redirect('/contact/?valid')
        
    return render(request, 'contact/contact.html', {'contact_form':contact_form})
