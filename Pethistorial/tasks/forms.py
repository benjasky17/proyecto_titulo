from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# La clase CustomUserCreationForm es una subclase de UserCreationForm que especifica los campos para la
# creación de usuarios.
class CustomUserCreationForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
		
