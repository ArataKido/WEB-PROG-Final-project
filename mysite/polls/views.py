from django.shortcuts import redirect, render
from .forms import ContactForm
from .models import ContactUs
def index(request):
    return render(request, "polls/index.html")

def about(request):

    return render(request, "polls/about.html")

def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cd = form.cleaned_data
            to_save = ContactUs(
                name = cd["name"],
                phone = cd["phone"],
                email = cd["email"],
                message = cd["message"],
            )
            to_save.save()
            return redirect('home')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
        context={
            'form': form 
        }
        return render(request, "polls/contact.html", context )

def services(request):
    return render(request, "polls/services.html")

def portfolio(request):
    return render(request, "polls/portfolio.html")

def get_background(request):
    background = { 'home' : "home_bg", 'about' : "about_bg" , 'contact' : "contact_bg", 'services' : "services_bg", 'portfolio' : "portfolio_bg",}
    return render (request, "polls/base.html", {"background" : background},   )
