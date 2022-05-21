from random import random
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from fundraise.models import Charity
# Create your models here.

class Donation(models.Model):
    fundraise = models.ForeignKey(Charity, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(default=0)
    isAnonymous = models.BooleanField(default=False)
    donarName = models.CharField(max_length=100)
    donationMessage = models.CharField(max_length=255)
    def __str__(self):
        return self.donarName

class Donated(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    isDonated = models.BooleanField(default = False)
    def __str__(self):
        return self.donation.donarName


class Payment(models.Model):
    amount = models.IntegerField()
    token = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.token} - {self.amount}"
