from django.shortcuts import render


# Create your views here.


def other(request):
    return render(request, 'basic_app/other.html', context={})


def index(request):
    context_dict = {'text': 'Hello world', 'number' : 10, 'numbers' : list(range(11))}
    return render(request, 'basic_app/index.html', context_dict)


def relative(request):
    return render(request, 'basic_app/relative_url_templates.html', context={})


def base(request):
    return render(request, 'basic_app/base.html', context={})
