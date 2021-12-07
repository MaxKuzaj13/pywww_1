from django.contrib.auth import authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .form import UserCreationForm, RegistrationForm


def registration(request):
    form = RegistrationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Ad user to staff
            form.save_as_staff()
            print('hu')
            return redirect('posts/list/')
        else:
            return render(request, '/loginregister/register.html', context)
    else:
        return render(request, '/loginregister/register.html', context)


def login(request):
    context = {}
    return render(request, 'loginregister/login.html', context)


def logout(request):
    context = {}
    return render(request, 'logout.html', context)
