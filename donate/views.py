from django.shortcuts import render
from .forms import DonationForm
# Create your views here.

def donateform(request):
    return render(request, 'donationform.html', {'form':DonationForm()})
