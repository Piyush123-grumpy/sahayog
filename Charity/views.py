from django.shortcuts import redirect, render
from .forms import CharityForm
# Create your views here.

def CharityPage(request):
    if request.method != "POST":
        form = CharityForm()
        return render(request, 'charity.html', {'form':form})
    else:
        form = CharityForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('error')
        return redirect('/')