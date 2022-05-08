from django.shortcuts import redirect, render
from .forms import ContactForm, CommentsForm
from .models import ContactUs, Comments
def index(request):
    return render(request, "polls/index.html")

def about(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        comment = CommentsForm(request.POST)
        # check whether it's valid:
        if comment.is_valid():
            cd = comment.cleaned_data
            to_save = Comments(
                name = cd["name"]
            )
            to_save.save()
            return redirect('home')

    else:
        comment = CommentsForm()
        context={
            'comment': comment 
            }
        return render(request, "polls/about.html", context )



def contact(request):
    """routes user to contact page and either creates blank form or saves data from form in database 

    Args:
        request: creates HttpRequest object which contains data about users request 

    Returns:
        str: If the django is requesting GET then function will route user to the page contact.html 
            and at the same time it will create a form.
            If this is POST request then creates an instance and fills it with data.
            If data is valid then it saves everything in database and sends the user to home view
    """
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
