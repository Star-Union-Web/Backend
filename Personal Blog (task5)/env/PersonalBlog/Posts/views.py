from django.shortcuts import render
from .models import Post, Comment
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.

def post(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'Posts/home.html', {'posts': posts})

def view_post(request, slug):
    if request.method == 'GET':
        post = Post.objects.get(slug=slug)
        if post.is_published or post.author == request.user:
            return render(request, 'Posts/home.html', {'post': post})
        else:
            return HttpResponseForbidden('You do not have permission to view this post')

@login_required
def delete_post(request, post_id):
        if request.method == 'POST':
            if not request.user.is_authenticated:
                return HttpResponseForbidden('You do not have permission to delete this post')
        
            post = Post.objects.get(id=post_id)

            if  post.author == request.user:
                post.delete()
                return redirect('posts')
            
            else:
                return HttpResponseForbidden('You do not have permission to delete this post')
        
            
        
@login_required
def create_post(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return redirect('login')
        
        form = PostForm()
        return render(request, 'Posts/create.html', {'form': form})
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = PostForm(request.POST)
            if form.is_valid():
                form.instance.author = request.user
                form.save()
                return redirect('posts')
            else:
                return render(request, 'Posts/create.html', {'form': form, 'type': 'Create'})

    else:
        return redirect('login')
    
@login_required
def edit_post(request, post_id):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return redirect('login')
        
        post = Post.objects.get(id=post_id)
        if post.author != request.user:
            return HttpResponseForbidden('You do not have permission to edit this post')
        
        form = PostForm(instance=post)
        return render(request, 'Posts/create.html', {'form': form, 'type': 'Edit'})
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            post = Post.objects.get(id=post_id)

            if post.author != request.user:
                return HttpResponseForbidden('You do not have permission to update this post')
            
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('posts')
            else:
                return render(request, 'Posts/home.html', {'form': form})
        else:
            return redirect('login')
    
