from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Contenido')