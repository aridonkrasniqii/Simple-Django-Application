from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'basic_app/index.html', context={})


def other(request):
    return render(request, 'basic_app/other.html', context={})


def relative(request):
    return render(request, 'basic_app/relative_url_templates.html', context={})


def base(request):
    return render(request, 'basic_app/base.html', context={})
