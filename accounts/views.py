from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,logout
from django.contrib import messages
from accounts.models import User
from django.http import HttpResponseRedirect

# Create your views here.
<<<<<<< HEAD

def loginProcess(request):
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

def loginProcess(request):
    if request.method == 'POST':
            first_name = request.POST['first_name']
            username = request.POST['username']
            email = request.POST['email']
            password1 =request.POST['password1']
            password2 =request.POST['password2']
            user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name)
            user.save();
            print("User created")
            return redirect('login')

    return render(request,"register.html")
            
=======
def loginPage(request):
    return render(request,'accounts/login.html')
>>>>>>> accounts
