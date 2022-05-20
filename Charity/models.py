from platform import mac_ver
from django.db import models
# Create your models here.


class Category(models.Model):
    categoryName = models.CharField(max_length=100)


class Charity(models.Model):
    for_who = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    email = models.CharField(max_length=100)

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='Charity')
    khalti = models.CharField(max_length=10)
    created_date = models.DateField(auto_now_add=True)
    requestedAmount = models.IntegerField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

