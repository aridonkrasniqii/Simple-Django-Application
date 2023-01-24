from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserForm, UserProfileInfoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    context = {}
    return render(request, 'basic_app/index.html', context=context)


@login_required
def special(request):
    return HttpResponse('You are logged in, Nice!')


# if is login it will be executed
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST or None)
        profile_form = UserProfileInfoForm(data=request.POST or None)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  # hashing the password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user  # one to one relationship

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'basic_app/registration.html', context=context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                # return HttpResponseRedirect(reverse('index'))
                return redirect('basic_app:index')
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:

            print('Someone tried to login and failed! ')
            print("Username {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied! ")
    else:
        return render(request, 'basic_app/login.html', context={})
