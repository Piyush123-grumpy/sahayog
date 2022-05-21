from django.shortcuts import redirect, render
from .forms import DonationForm
from fundraise.models import Charity
# Create your views here.

def donateform(request):
    if(request.method=='POST'):
        form = DonationForm(request.POST)
        fundraise = request.POST['fundraise']
        print('fundraise::::::::::: ',Charity.objects.get(id = fundraise))
        print('user:::::::::::::', request.user)
        print(fundraise)
        if(form.is_valid()):
            f = form.save()
            if form.cleaned_data.get('isAnonymous'):
                f.user = None
                f.fundraise = Charity.objects.get(id = fundraise)
                f.save()
            else:
                f.user = request.user
                f.fundraise = Charity.objects.get(id = fundraise)
                f.save()
        return render(request, 'donationform.html', {'form':DonationForm(), 'fundraise':fundraise})

        # else:
        #     fundraise = request.POST['fundraise']
        #     return render(request, 'donationform.html', {'form':DonationForm()})
    else:
        return redirect('')