from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from fundraise.models import Charity
# Create your models here.

class Donation(models.Model):
    fundraise = models.ForeignKey(Charity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    isAnonymous = models.BooleanField(default=False)
    donarName = models.CharField(max_length=100)
    donationMessage = models.CharField(max_length=255)

class Donated(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    isDonated = models.BooleanField(default = False)




