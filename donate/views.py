import random

from django.shortcuts import redirect, render

from donate.models import Payment
from django.shortcuts import render

from fundraise.models import Charity
from .forms import DonationForm
from fundraise.models import Charity
# Create your views here.

def donateform(request, id):
    fundraiseDetail = Charity.objects.get(id = id)
    
    if(request.method=='POST'):
        form = DonationForm(request.POST)
        # fundraise = request.POST['fundraise']
        charity = Charity.objects.get(id = id)

        
        if(form.is_valid()):
            f = form
            if form.cleaned_data.get('isAnonymous'):
                f.user = None
                f.fundraise = charity
                f.save()
            else:
                f.user = request.user
                f.fundraise = charity
                f.save()
            payment = Payment.objects.create(token = f"TKN-{random.randint(1000,9999)}", amount = form.cleaned_data.get('amount'))
            print('PAYMENT DONE')
        return render(request, 'donationform.html', {'form':DonationForm(),'fundraise': charity, 'fundraiseDetail':fundraiseDetail})


    else:
        form = DonationForm()

    return render(request, 'donationform.html', {'form':DonationForm(), 'fundraiseDetail':fundraiseDetail})
# def donateform(request,id):

#     fundraiseDetail = Charity.objects.get(id = id)
#     return render(request, 'donationform.html', {'form':DonationForm(), 'fundraiseDetail':fundraiseDetail})
