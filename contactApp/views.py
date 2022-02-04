from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
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
            
            email = EmailMessage('Lead Message', '{} dice:\n\n{}'.format(name, content), '', ['nazamartedi@gmail.com'], reply_to=[email] )
            
            try:
                # If success
                email.send()
                return redirect('/contact/?valid')
            except:
                return redirect('/contact/?notvalid')
        
    return render(request, 'contact/contact.html', {'contact_form':contact_form})
