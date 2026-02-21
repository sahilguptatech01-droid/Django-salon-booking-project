from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class RegisterForm(UserCreationForm):
    email=forms.EmailField()
    phone_no=forms.IntegerField()
    class Meta:
        model=User
        fields=['username','phone_no','email','password1','password2']