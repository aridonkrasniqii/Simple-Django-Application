from email import contentmanager
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    context = {'variable': "<br>Welcome to Django level two"}
    return render(request, 'index.html', context=context)



