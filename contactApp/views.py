from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    
    # We need to instantiate a ContactForm object in order to show it on the template
    contact_form = ContactForm()
    return render(request, 'contact/contact.html', {'contact_form':contact_form})
