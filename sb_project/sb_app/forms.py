from django import forms
from sb_app.models import UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','password','email')


class UserProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ('user','profile_pic')