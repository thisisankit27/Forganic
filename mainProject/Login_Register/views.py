from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import JsonResponse

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['CustomerUsername']
        password = request.POST['CustomerPassword']
        user = auth.authenticate(username = username, password=password)
        if user is not None:
            auth.login(request, user)
            return JsonResponse({'success': True, 'url': '/'})
        else:
            if User.objects.filter(username=username).exists():
                return JsonResponse({'success': False, 'message': 'Wrong Password!'})
            else:
                return JsonResponse({'success': False, 'message': 'Username Does Not Exist!'})
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
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'message': 'Username Already Exists!'})
        elif User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'Email Already Exists!'})
        else:
            if password == password2:
                userObj = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
                userObj.save()
                return JsonResponse({'success': True, 'url': 'login'})
            else:
                return JsonResponse({'success': False, 'message': "Passwords don't Match!"})
    else:
        return render(request, 'Login_Register/Register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def forgotPassword(request):
    return render(request, 'Login_Register/forgot-your-password.html')