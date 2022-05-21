from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,logout
from django.contrib import messages
from pkg_resources import require
from accounts.forms import CreateUserForm,Userinfo
from accounts.models import User, User_info
from django.http import HttpResponseRedirect
from PIL import Image  
import PIL  


# Create your views here.

def loginPage(request):
    if request.method == 'POST':      
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username, password=password)

            if username and password !="":
                if user is not None:
                    auth_login(request,user)
                    return redirect('home:index')
                else:
                    messages.info(request, "Username or password is incorrect")
            else:
                messages.info(request, "Enter username and password")
    return render(request, 'accounts/login.html')
            
def registerPage(request):
    current_user = request.user
    if request.user.is_authenticated:
        return redirect ('home:index')
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

def logoutUser(request):
    logout(request)
    return redirect('home:index')
def userinfo(request):
    # user=request.user.id
    # info=User_info.objects.get(User_id=user)
    # print("ok")
    # print(info.city)     
    # print(info.address) 
    # print(info.phone_number)        
    # if request.method =="POST":
    #     form=Userinfo(request.POST,instance=info)
    #     print(form)
    #     if form.is_valid():
            
    #         form.save()
    if request.method =="POST":
        city=request.POST.get('City')
        address=request.POST.get('Address')
        phone_number=request.POST.get('Phone_number')
        picture=request.POST.get('Profile_picture')
      
        if User_info.objects.filter(User_id=request.user.id).exists():
            print("okay")
            User_info.objects.filter(User_id=request.user.id).update(city=city,address=address,phone_number=phone_number,profile_picture=picture)
        
        

    form=Userinfo()
    return render(request,"accounts/User_profile.html",{'form':form})

def profile(request):

    info=User_info.objects.get(User_id=request.user.id)

    # name=info.User_id.username
    print(info)
    return render(request,"accounts/profile.html",{'info':info})