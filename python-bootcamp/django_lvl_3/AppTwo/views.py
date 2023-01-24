from django.shortcuts import render
from AppTwo.models import User
from AppTwo.forms import NewUserForm


# Create your views here.


def index(request):
    return render(request, 'AppTwo/index.html', context={})


def users(request):
    form = NewUserForm()
    users = User.objects.all()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    my_context = {'form': form, 'users': users}
    return render(request, 'AppTwo/users.html', context={'dict': my_context})



