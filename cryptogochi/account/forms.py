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
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

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

'''
class UserLogin(forms.Form):
    username = forms.CharField(max_length = 255)
    password = forms.CharField()

    class Meta:
        model = User
        fields = ('username')
        help_texts = {
            'username': None,
            'email': None,
            'first_name': None,
        }

class RegistrationForm(forms.ModelForm):
    password = forms.CharField()
    password2 = forms.CharField()

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
'''