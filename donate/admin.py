from django.contrib import admin

# Register your models here.
from .models import Donated, Donation

# Register your models here.
admin.site.register(Donation)
admin.site.register(Donated)



