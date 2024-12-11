from django import forms
from .models import Post,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import UpdateView

class add_data(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','image','slug','content','published_status']

        
class Register_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

