from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages


def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm()
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return(redirect('login'))
    return render(request, template_name=('users/signup.html'), context={'form': form})

def login(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm()(request.POST)
        if form.is_valid():
            form.save()
    return render(request, template_name=('users/login.html'))
