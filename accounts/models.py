from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.
class User(AbstractUser):
    phone_number=models.CharField(verbose_name="Phone Number",max_length=30)
    product_image=models.ImageField(upload_to='shop/images',default='', null=True, blank=True)