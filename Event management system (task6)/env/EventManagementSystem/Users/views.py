from django.shortcuts import render
from django.http import HttpResponseForbidden
from .forms import RegisterForm, LoginForm, AdminRegisterForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from .models import CustomUser as User
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required, login_required
from events.models import Event

# Create your views here.

def user_login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('profile')
        
        form = LoginForm()
        return render(request, 'Users/login.html', {'form': form})

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if not form.is_valid():
            return render(request, 'Users/login.html', {'form': form})

        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.filter(email=email).first()
        
        if user is not None and user.check_password(password):
            login(request, user)
            print(request.user.is_authenticated)
            return redirect('profile')
        
        return render(request, 'Users/login.html', {'error': 'Invalid credentials', 'form': form})
        

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return redirect('login')
        

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
            user = User.objects.get(email=form.cleaned_data['email'])
            group = Group.objects.get(name='user')
            user.groups.add(group)
            
            return redirect('login')
        else:
            return render(request, 'Users/register.html', {'form': form, 'error': 'Invalid data'})


@permission_required('event.admin')
def admin_register(request):
    if request.method == 'GET':
        form = AdminRegisterForm()
        return render(request, 'Users/register.html', {'form': form})
    
    if request.method == 'POST':
        form = AdminRegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            user_type = form.cleaned_data['user_type']
            group = Group.objects.get(name=user_type)
            user.groups.add(group)
            return render(request, 'Users/register.html', {'form': form, 'success': 'User registered successfully'})
        
        return render(request, 'Users/register.html', {'form': form})
            

            
@login_required(login_url='login')
def profile(request):
    if request.method == 'GET':
        events = Event.objects.filter(organizer=request.user)
        return render(request, 'Users/profile.html', {'events': events})
