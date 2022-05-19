from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,logout
from django.contrib import messages
from accounts.models import User
from django.http import HttpResponseRedirect

# Create your views here.
def loginPage(request):
    return render(request,'accounts/login.html')
