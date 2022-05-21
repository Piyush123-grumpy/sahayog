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
    user=request.user.id
    info=User_info.objects.get(User_id=user)
    print("ok")
    print(info.city)     
    print(info.address) 
    print(info.phone_number)        
    # if request.method =="POST":
    #     form=Userinfo(request.POST,request.FILES,instance=info)
    #     print(form)
    #     if form.is_valid():
    form=Userinfo()

            
    if request.method =="POST"or request.method == "FILES":
        city=request.POST.get('City')
        address=request.POST.get('Address')
        phone_number=request.POST.get('Phone_number')
        picture=request.FILES.get('Profile_picture')
      
        if city:
            info.city = city
        if address:
            info.address = address
        if phone_number:
            info.phone_number = phone_number
        if picture:
            info.profile_picture = picture
        
        info.save()
        
        return render(request,"accounts/User_profile.html",{'form':form, 'info':info})

    return render(request,"accounts/User_profile.html",{'form':form, 'info':info})

def profile(request):

    info=User_info.objects.get(User_id=request.user.id)

    # name=info.User_id.username
    print(info)
    return render(request,"accounts/profile.html",{'info':info})