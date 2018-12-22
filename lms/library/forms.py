from django.contrib.auth import get_user_model
from django import forms
from . models import issuedetail
User=get_user_model()


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']


class UserLoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','password']


class IssueDetailForm(forms.ModelForm):

    class Meta:
        model = issuedetail
        fields = ['Book']