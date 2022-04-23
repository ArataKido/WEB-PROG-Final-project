from .models import ContactUs
from django.forms import ModelForm, TextInput ,Textarea

class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'phone', 'email', 'message']
        widget = {
            "name": TextInput(attrs={
                'placeholder': 'Name', 
                'class': 'form-group',
                'id' : 'input_name',
            }),
            "phone": TextInput(attrs={
                'placeholder': 'Phone', 
                'class': 'form-group',
                'id' : 'input_name',

            }),

            "email": TextInput(attrs={
                'placeholder': 'Email', 
                'class': 'form-group',
                'id' : 'input_name',

            }),


        }

