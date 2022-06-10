from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_v, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.logout_v, name="logout"),
]