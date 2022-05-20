from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,logout
from django.contrib import messages
from accounts.forms import CreateUserForm
from accounts.models import User, User_info
from django.http import HttpResponseRedirect

# Create your views here.
<<<<<<< HEAD

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
    current_user = request.user
    if request.user.is_authenticated:
        return redirect ('index')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            print(request.POST)
            print("Got data")
            form = CreateUserForm(request.POST)
            if form.is_valid():
                print("form valid")
                f = form.save()
                f.save()

                print(f.username)
                print("form saved")
                User_info.objects.create(User=f)
                return redirect('accounts:success')
            else:
                messages.error(request, "Error")
                
        context ={
            'form':form,
        }
    return render(request, 'accounts/registration.html',context)

def success(request): 
    return render(request, "accounts/success.html")
=======
def loginPage(request):
    return render(request,'accounts/login.html')
>>>>>>> forgetpassword
