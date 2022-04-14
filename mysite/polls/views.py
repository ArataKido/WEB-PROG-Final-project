from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "polls/index.html")

def about(request):
    return render(request, "polls/about.html")

def contact(request):
    return render(request, "polls/contact.html")

def services(request):
    return render(request, "polls/services.html")

def portfolio(request):
    return render(request, "polls/portfolio.html")

