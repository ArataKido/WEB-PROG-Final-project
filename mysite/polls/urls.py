from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name ='home'),
    path('about-us', views.about, name ='about' ),
    path('contact-us', views.contact, name = 'contact'  ),
    path('services', views.services, name = 'services'),
    path('portfolio', views.portfolio, name = 'portfolio'),
    path('admin/', admin.site.urls) 
    ]