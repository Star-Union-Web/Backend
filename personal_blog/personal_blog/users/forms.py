from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)

class UpdateProfilePicForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']