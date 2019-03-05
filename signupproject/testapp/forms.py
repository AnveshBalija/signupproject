from django import forms
from django.core import validators

class SignupForm(forms.Form):
    name=forms.CharField(validators=[validators.MinLengthValidator(4)])
    password=forms.CharField(widget=forms.PasswordInput)
    repassword=forms.CharField(label='Reenter password', widget=forms.PasswordInput)
    email = forms.EmailField()

