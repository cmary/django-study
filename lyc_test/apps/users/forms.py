#---encoding=utf-8
__author__ = 'lyc'
__date__ = '18-2-27 下午11:22'

from django import forms
from .models import UserProfile
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(required=True,min_length=5)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    #email  = forms.EmailField(required=True)
    username = forms.CharField(required=True, min_length=5)
    password = forms.CharField(required=True, min_length=5, max_length=16)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})