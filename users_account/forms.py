from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User

class CreateSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields =['username','first_name', 'last_name', 'email', 'password1', 'password2']
        #fields ='__all__'
        

    def __init__(self, *args,  **kwargs):
        super(CreateSignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class ChangePasswordForm(PasswordChangeForm):
    pass