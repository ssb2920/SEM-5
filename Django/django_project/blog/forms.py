from django import forms
from .models import Post , Entry

class EntryForm(forms.ModelForm):
   class Meta:
        model = Entry
        fields = ['rollno','year','branch']