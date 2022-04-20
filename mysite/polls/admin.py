from django.contrib import admin
from .models import Email, Message, Name, Phone

admin.site.register(Name)
admin.site.register(Email)
admin.site.register(Phone)
admin.site.register(Message)


