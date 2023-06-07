from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import User

class CustomUserForm(UserCreationForm):

	email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder': 'Your Email*'}))
	first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder' : 'Your First Name*'}))
	last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder' : 'Your Last Name*'}))
	password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder' : 'Password*'}))
	password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder' : 'Confirm Paswword*'}))


	class Meta:
		model = User
		fields = ['email','first_name','last_name','password1','password2']

class CustomLoginForm(AuthenticationForm):
	username = UsernameField(label="", widget=forms.EmailInput(attrs={'placeholder': 'Enter Email'}))
	password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))