from django.shortcuts import render
from .forms import ContactForm

def index(request):
    return render(request, "polls/index.html")

def about(request):
    return render(request, "polls/about.html")

def contact(request):
    form = ContactForm()
    context={
        'form': form 
    }
    return render(request, "polls/contact.html", context )

def services(request):
    return render(request, "polls/services.html")

def portfolio(request):
    return render(request, "polls/portfolio.html")
