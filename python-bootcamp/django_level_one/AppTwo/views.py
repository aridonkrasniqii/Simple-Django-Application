from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request):
    context = {'insert_me': 'Not I am coming from first_app/index.html'}

    return render(request, 'first_app/index.html', context=context)


