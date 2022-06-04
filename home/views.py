from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html')
def signup_login(request):
    return render(request, 'main/signup-login.html')

