from django.forms import ModelForm
from .models import Charity

class CharityForm(ModelForm):
        class Meta:
            model = Charity
            fields = ['title', 'description', 'thumbnail', 'khalti', 'requestedAmount']