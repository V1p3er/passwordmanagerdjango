from django.shortcuts import render


def signup_login(request):
	return render (request=request, template_name="users/users.html")