from django.shortcuts import render
from basicapp.forms import FormName


# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html', context={})


def form_name(request):
    form = FormName(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data['name'], " " , form.cleaned_data['email'])
    return render(request, 'basicapp/form_page.html', context={"form": form})



