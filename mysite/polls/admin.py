from django.contrib import admin
from .models import ContactUs, Comments

# registers those classes in db
admin.site.register(ContactUs)
admin.site.register(Comments)
