from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'Users/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponse('User logged in successfully')
        else:
            return HttpResponse('Invalid credentials')

def logout(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        return HttpResponse('User is not logged in')


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'Users/register.html', {'form': form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully')
        else:
            return render(request, 'Users/register.html', {'form': form})
        
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'Users/profile.html', {'user': request.user})
    else:
        return HttpResponse('User is not logged in')
        