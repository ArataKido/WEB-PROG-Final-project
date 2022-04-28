from email import message
from .models import ContactUs
from django import forms

class ContactForm(forms.Form):
    
    name = forms.CharField(widget=forms.TextInput(attrs={
        'name' : "fullname" ,
        'type' : "text" ,
        'class' : "form-control" ,
        'id' : "input_name",
        'placeholder' : "Name" ,
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'name': "email", 
        'type' :"email" ,
        'class':"form-control", 
        'id':"input_email" ,
        'placeholder':"Email",
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'name' : "phone" ,
        'type' : "tel" ,
        'class':"form-control", 
        'id': "input_tel" ,
        'placeholder' : "Phone",
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
    'name' : "message",
    'rows' : "6",
    'class' : "form-control",
    'id' : "input_message" ,
    'placeholder' : "Message...",
    
    
    }))







