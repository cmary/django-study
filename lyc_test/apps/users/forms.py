#---encoding=utf-8
__author__ = 'lyc'
__date__ = '18-2-27 下午11:22'

from django import forms
from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(required=True,min_length=5)
    password = forms.CharField(required=True, min_length=5)