from django import forms
from .models import StudentUser
from django.contrib.auth.forms import UserCreationForm

class StudentRegisterForm(UserCreationForm):
    class Meta:
        model = StudentUser
        fields = ['email','rollno','name']

class StudentLoginForm(forms.Form):
    username = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)