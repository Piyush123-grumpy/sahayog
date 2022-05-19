from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,logout
from django.contrib import messages
from accounts.models import User
from django.http import HttpResponseRedirect

# Create your views here.

def loginPage(request):
    if request.method == 'POST':      
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username, password=password)

            if username and password !="":
                if user is not None:
                    auth_login(request,user)
                    return redirect('index')
                else:
                    messages.info(request, "Username or password is incorrect")
            else:
                messages.info(request, "Enter username and password")
    return render(request, 'accounts/login.html')
            
def registerPage(request):
    return render(request, 'accounts/registration.html')