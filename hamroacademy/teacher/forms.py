from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    #     widgets = {'username':forms.TextInput(attrs={'class':'form-control border-0 p-4',
    #    }),
    #    'firstname':forms.TextInput(attrs={'form-control border-0 p-4',
    #    }),
    #     'last_name':forms.TextInput(attrs={'form-control border-0 p-4',
    #    }),
    #     'email':forms.EmailField(attrs={'form-control border-0 p-4',
    #    }),
    #    'password1':forms.PasswordInput(attrs={'class':'form-control border-0 p-4'}),
    #     'password2':forms.PasswordInput(attrs={'class':'form-control border-0 p-4'}),
    #     }