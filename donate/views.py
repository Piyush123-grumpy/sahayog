from django.shortcuts import render

from fundraise.models import Charity
from .forms import DonationForm
# Create your views here.

def donateform(request,id):

    fundraiseDetail = Charity.objects.get(id = id)
    return render(request, 'donationform.html', {'form':DonationForm(), 'fundraiseDetail':fundraiseDetail})
