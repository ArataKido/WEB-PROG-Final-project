from .models import Name, Phone, Email, Message
from django.forms import ModelForm, TextInput, Textarea

class NameForm(ModelForm):
    class Meta:
        model = Name
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-group',
                'placeholder': 'Name', 
            })
        }

