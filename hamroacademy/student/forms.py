from dataclasses import field
from operator import attrgetter
from django import forms
from .models import User


class StudentRegistration(forms.ModelForm):
 class Meta:
    model=User
    fields=['name','email','password']  
             
