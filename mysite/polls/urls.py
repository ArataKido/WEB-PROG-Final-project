from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about,),
    path('contact-us', views.contact),
    path('services', views.services),
    path('portfolio', views.portfolio),
]