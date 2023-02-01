from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import TravelAgentProfile
from django.contrib.auth.models import User


class TravelAgentSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class TravelAgentProfileForm(forms.ModelForm):
    class Meta:
        model = TravelAgentProfile
        fields = ["keywords", "profile", "calendly_link"]