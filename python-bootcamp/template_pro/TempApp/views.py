from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'variable': 'Welcome To Django  This is my first template solution'}
    return render(request, 'index.html', context=context)
