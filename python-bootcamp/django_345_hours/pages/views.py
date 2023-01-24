from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)  # teknikashi
    # return HttpResponse("<h1>Hello from Python Django Web Framework </h1>")
    return render(request, 'home.html', context={})


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', context={})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 23,
        "my_summary": "Sunny Hill Festival",
        "my_numbers": [111, 22, 333, 5213431, 'aridon'],
        'html': "<em> Italic text for html </em>"
    }
    return render(request, 'about.html', context=my_context)


def social_view(request, *args, **kwargs):
    return render(request, 'social.html', context={})
