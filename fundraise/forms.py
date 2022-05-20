from django import forms
from django.forms import ModelForm
from .models import Charity

class CharityForm(ModelForm):
        first_name = forms.CharField(max_length=155,
                            widget= forms.TextInput(
                                attrs={'placeholder': 'First Name'}))
        last_name = forms.CharField(max_length=155,
                    widget= forms.TextInput(
                        attrs={'placeholder': 'Last Name'}))

        email = forms.CharField(max_length=155,
                    widget= forms.TextInput(
                        attrs={'placeholder': 'Email'}))

        city = forms.CharField(max_length=155,
                    widget= forms.TextInput(
                        attrs={'placeholder': 'City'}))
        zip_code = forms.CharField(max_length=155,
                    widget= forms.TextInput(
                        attrs={'placeholder': 'Zipcode'}))

        title = forms.CharField(max_length=155,
                    widget= forms.TextInput(
                        attrs={'placeholder': 'Title'})) 
        khalti = forms.CharField(max_length=155,
                    widget= forms.TextInput(
                        attrs={'placeholder': 'Khalti Phonenumber'}))  
        description = forms.CharField(max_length=155,
                    widget= forms.TextInput(
                        attrs={'placeholder': 'Description'}))  
        requestedAmount = forms.IntegerField(
                    widget= forms.NumberInput(attrs={'min': '0','placeholder': 'Requested Amount'}))
        # choices=[('Wedding','Wedding'),('Wedding','Wedding'), ('Rice feeding ceremony ','Rice feeding ceremony'), ('Bratabanda','Bratabanda'),('Bel Bibaha','Bel Bibaha'),('All Events','All Events')]
        # # category = forms.ChoiceField(choices=choices,
        # #                             widget=forms.Select(
        # #                                 attrs={'class':'form-control'}))
        class Meta:
            model = Charity
            fields = ['first_name', 'last_name', 'city', 'zip_code', 'email', 'title', 'description', 'thumbnail', 'khalti', 'requestedAmount', 'category']

