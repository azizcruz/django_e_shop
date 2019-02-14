from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'country', 'address')

class RequestActivationLinkForm(forms.Form):
    username = forms.CharField(label='Username')