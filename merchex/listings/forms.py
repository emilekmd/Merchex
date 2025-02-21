from django import forms
from .models import Band, Listing

class ContactUsForm (forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class BandsForm(forms.ModelForm):
    class Meta:
        model = Band
        exclude = ('active', 'official_homepage')

class ListForm(forms.ModelForm):
    class Meta:
        model = Listing
        exclude = ('sold',)