from django import forms
from .models import Tour
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")


class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = ("title", "category", "town", "stars", "image", "price", "description", "nights")