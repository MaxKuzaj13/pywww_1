from django.contrib.auth import authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from .form import UserCreationForm, RegistrationForm


def registration(request):
    form = RegistrationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Ad user to staff
            form.save_as_staff()
            return redirect(reverse('/'))
    else:
        form = RegistrationForm()
        context = {'form': form}
    return render(request, 'login_register/register.html', context)

#
# def login(request):
#     print('test')
#     context = {}
#     return render(request, 'login_register/login.html', context)
#
#
# def logout(request):
#     context = {}
#     return render(request, 'logout.html', context)
