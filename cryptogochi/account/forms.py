from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        help_texts = {
            'username': None,
            'email': None,
            'first_name': None,
        }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password')
    password2 = forms.CharField(label='Repeat password')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        help_texts = {
            'username': None,
            'email': None,
            'first_name': None,
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']