from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from . import models

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['CustomerUsername']
        password = request.POST['CustomerPassword']
        user = auth.authenticate(username = username, password=password)
        response_dict = models.CustomerProfile.verify_user(user, username)
        if user is not None:
            auth.login(request, user)
            return JsonResponse(response_dict)
        else:
            if User.objects.filter(username=username).exists():
                return JsonResponse(response_dict)
            else:
                return JsonResponse(response_dict)
    else:
        return render(request, 'Login_Register/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['CustomerUsername']
        email = request.POST['CustomerEmail']
        first_name = request.POST['CustomerFirstName']
        last_name = request.POST['CustomerLastName']
        password = request.POST['CustomerPassword']
        password2 = request.POST['CustomerConfirmPassword']
        
        response_dict = models.CustomerProfile.create_profile(username, email, first_name, last_name, password, password2)

        return JsonResponse(response_dict)
    else:
        return render(request, 'Login_Register/Register.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')