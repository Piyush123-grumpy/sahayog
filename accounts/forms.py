from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from accounts.models import User_info

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['first_name', 'last_name','username', 'email', 'password1', 'password2']
class Userinfo(ModelForm):
    
    class Meta:
        model=User_info
        fields='__all__'