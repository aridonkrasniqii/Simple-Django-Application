from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            messages.success(request, f"Your account has been created! You are able to log in !")
            return redirect('login')


    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', context={'form': form})


"""
    message.debug
    message.info
    message.success
    message.warning
    message.error
"""



@login_required
def profile(request):


    return render(request, 'users/profile.html', context = {})
