from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return(redirect('login'))
    else:
        form = CreateUserForm()
    return render(request, template_name=('users/signup.html'), context={'form': form})

def login_v(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user.is_authenticated:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login/')
    return render(request, template_name=('users/login.html'))

def dashboard(request):
    return render(request, template_name=('users/dashboard.html'))