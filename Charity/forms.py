from django.forms import ModelForm
from .models import Charity

class CharityForm(ModelForm):
        class Meta:
            model = Charity
            fields = ['for_who','first_name', 'last_name', 'city', 'zip_code', 'email', 'title', 'description', 'thumbnail', 'khalti', 'requestedAmount', 'category']