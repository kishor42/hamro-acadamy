from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.forms import CompanyCreationForm
from django.contrib.auth.models import Company

from administration.models import Course


class CompanyRegistrationForm(CompanyCreationForm):
    
    CompanyName = forms.CharField(max_length=101)
    CompanyAddress = forms.CharField(max_length=101)
    Logo = forms.ImageField(upload_to='uploads/')
    phoneno=forms.IntegerField()  
      
    class Meta:
        model = Company
        fields = ['CompanyName', 'CompanyAddress', 'Logo', 'phoneno']



# class CourseRegistration(forms.ModelForm):
#  class Meta:
#     model=Course
#     fields=['course_number','course_name','max_numb_students','instructors']
#     widgets = {'name':forms.TextInput(attrs={'class':'form-control',
#     'id':'nameid'}),
#     'email':forms.EmailInput(attrs={'class':'form-control',
#     'id':'emailid'}),
#     'password':forms.PasswordInput(attrs={'class':'form-control','id':'passwordid'}),
#    }