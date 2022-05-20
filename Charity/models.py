from django.db import models

# Create your models here.
class Charity(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='Charity')
    khalti = models.CharField(max_length=10)
    requestedAmount = models.IntegerField()

