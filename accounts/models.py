from distutils.log import info
from turtle import mode
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class User_info(models.Model):
    User=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.Case)
    city=models.CharField(verbose_name="city",max_length=30)
    address=models.CharField (verbose_name="Address",max_length=30)
    phone_number=models.CharField(verbose_name="Phone Number",max_length=30)
    profile_picture=models.ImageField(upload_to='user_profile_pic',default='', null=True, blank=True)
    

