from django.shortcuts import render
from django.http import HttpResponseForbidden
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.

def user_login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('profile')
        
        form = LoginForm()
        return render(request, 'Users/login.html', {'form': form})

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        else:
            return render(request, 'Users/login.html', {'form': form})

        user = authenticate(request, username=username, password=password)
        
        if user is None:
            return render(request, 'Users/login.html', {'error': 'Invalid credentials'})
        
        login(request, user)
        return redirect('posts')


        

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return HttpResponseForbidden('You are not logged in')


def register(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('profile')
        
        form = RegisterForm()
        return render(request, 'Users/register.html', {'form': form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'Users/register.html', {'form': form, 'error': 'Invalid data'})
        
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'Users/profile.html', {'user': request.user})
    else:
        return redirect('login')
        