from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=False, help_text='')
    username = forms.CharField(max_length=30, required=False, help_text='*')
    email = forms.EmailField(max_length=254, help_text='*')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )