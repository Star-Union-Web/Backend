from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password1', 'password2']
        labels = {
            'name': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'


class AdminRegisterForm(UserCreationForm):
    user_type = forms.ChoiceField(
        choices=[('user', 'User'), ('admin', 'Admin'), ('organizer', 'Organizer')],
        widget=forms.Select(attrs={'class': 'form-control'}))
        
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password1', 'password2', 'user_type']
        labels = {
            'name': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
            'user_type': 'User Type'
        }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email Address')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')