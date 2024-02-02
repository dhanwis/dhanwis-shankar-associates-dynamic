from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('home')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'User Name or Password Incorrect.'
    else:
        error = None
    return render(request, 'auth_app/admin-login.html', {'error': error})