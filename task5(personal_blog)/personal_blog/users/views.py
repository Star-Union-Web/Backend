from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm, UpdateProfilePicForm
from .models import UserProfile
from blog.models import Post, Comments

# Create your views here.

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')

        
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    form = UpdateProfileForm(instance=request.user)
    pic_form = UpdateProfilePicForm(instance=request.user.userprofile)
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, instance=request.user)
        pic_form = UpdateProfilePicForm(request.POST, request.FILES, instance=request.user.userprofile)
        #data = request.POST
        #print(data)
        if form.is_valid() and pic_form.is_valid():
            form.save()
            pic_form.save()
            #User.objects.filter(username=).first 
            return redirect('profile')
            #pass
            
    else:
        form = UpdateProfileForm(instance=request.user)
        pic_form = UpdateProfilePicForm(instance=request.user.userprofile)

    context = {
        'readuser': request.user,
        'form': form,
        'pic_form': pic_form,
        'blogs': Post.objects.all().filter(author=request.user.id),
        'comments': Comments.objects.all().filter(author=request.user.id)
    }

    return render(request, 'profile.html', context)

def read_profile(request, **kwargs):
    profile_id = kwargs.get('id')
    user = User.objects.all().filter(id=profile_id).first()
    user_posts = Post.objects.all().filter(author=user.id)
    user_comments = Comments.objects.all().filter(author=user.id)

    context = {
        'readuser': user,
        'blogs': user_posts,
        'comments': user_comments
    } 

    return render(request, 'profile.html', context)


