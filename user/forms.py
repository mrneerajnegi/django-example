from django import forms
from  django.contrib.auth.models import User
from user.models import UserProfileInfo

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','email','password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')