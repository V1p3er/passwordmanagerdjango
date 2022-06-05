from django.shortcuts import render, redirect


def signup_login(response):
	return render(response, 'users/users.html')
	