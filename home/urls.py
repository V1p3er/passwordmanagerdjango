from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="main"),
    path('signup-login', views.signup_login, name="signup-login"),
]
