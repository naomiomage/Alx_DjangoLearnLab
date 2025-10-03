# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Registration form that adds email
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

# Simple form to edit the user profile (username + email)
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")
