from django import forms
from myapp.models import UserProfileInfo
from django.contrib.auth.models import User

# from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
	
	password = forms.CharField(widget=forms.PasswordInput())
	icode = forms.CharField()
	firstname = forms.CharField()
	lastname = forms.CharField()

	class Meta():
		model = User
		fields = ('email', 'username', 'firstname', 'lastname', 'password', 'icode')
