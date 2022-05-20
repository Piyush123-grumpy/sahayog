from django.shortcuts import render

from fundraise.forms import CharityForm

# Create your views here.

def fundraisePage(request):
    if request.method != "POST":
        form = CharityForm()
        return render(request, 'charity.html', {'form':form})
    else:
        form = CharityForm(request.POST,request.FILES)
        form.save()
        
    return render(request, 'charity.html')


