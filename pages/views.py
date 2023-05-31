from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def blog_view(request, *args, **kwargs):
    return render(request, "blog.html", {})

def about_view(request, *args, **kwargs):
    my_context ={
        "my_text": "This is about me",
        "this_is_true": True,
        "my_number": 605,
        "my_list": [1255, 1252, "abc", 1225]
    }
    return render(request, "about.html", my_context)
