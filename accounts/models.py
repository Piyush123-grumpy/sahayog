from distutils.log import info
from turtle import mode
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class User_info(models.Model):
    User=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.Case)
    city=models.CharField(verbose_name="city",max_length=30, null=True, blank=True)
    address=models.CharField (verbose_name="Address",max_length=30, null=True, blank=True)
    phone_number=models.CharField(verbose_name="Phone Number",max_length=30, null=True, blank=True)
    profile_picture=models.ImageField(upload_to='user_profile_pic',default='', null=True, blank=True)

    def __str__(self):
        return self.User.username
    

