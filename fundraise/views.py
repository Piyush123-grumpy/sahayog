import re
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from fundraise.forms import CharityForm
from .models import Category, Charity

# Create your views here.
@login_required(login_url='')
def fundraisePage(request):
    if request.method == "POST":
        form = CharityForm(request.POST,request.FILES)
        choice = request.POST.get("choiceFor")
        if(form.is_valid()):
            print(form.is_valid())
            f=form
            if choice == "choice1":
                f.for_who = "For me or Someone Else"
            elif choice == "choice2":
                f.for_who = "For Charity"
            f.user = request.user
            f.fundraise  = Charity.objects.get(id=request.POST.get("fundraise"))
            f.save()
            return redirect ('/')
        else:
            return render(request, 'charity.html', {'form':form})
    else:
        form = CharityForm()
        return render(request, 'charity.html', {'form':form})



def viewCategory(request, category):
    fundraisers = Charity.objects.filter(category = category)
    return render(request, 'viewCategory.html', {'fundraisers':fundraisers})
        
    
def viewFundraise(request, charity):
    fundraise = Charity.objects.get(id=charity)
    print(fundraise.title)
    return render(request, 'viewFundraise.html', {'fundraise': fundraise})

