from django.shortcuts import render
from .models import Post, Comment
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, Http404

# Create your views here.

def post(request):
    if request.method == 'GET':
        posts = [post for post in Post.objects.all() if post.is_published or post.author == request.user]
        
        return render(request, 'Posts/home.html', {'posts': posts})


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
        return render(request, 'Posts/create_post.html', {'form': form, 'type': 'Create'})
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = PostForm(request.POST)
            if form.is_valid():
                form.instance.author = request.user
                form.save()
                return redirect('posts')
            else:
                return render(request, 'Posts/create_post.html', {'form': form, 'type': 'Create'})

    else:
        return redirect('login')
    
@login_required
def edit_post(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        if post.author != request.user:
            return HttpResponseForbidden('You do not have permission to edit this post')
        
        form = PostForm(instance=post)
        return render(request, 'Posts/create_post.html', {'form': form, 'type': 'Edit'})
    
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


@login_required
def comments(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post=post)
        return render(request, 'Posts/comments.html', {'post': post, 'comments': comments, "type": 'Create'})

    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        if not post: 
            return Http404('Post not found')
        comment = Comment()

        if post.is_published:
            comment.content = request.POST.get('content')
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('comments', post_id)
        else:
            return HttpResponseForbidden('You do not have permission to comment on this post')

        
    

@login_required       
def delete_comment(request, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=comment_id)
        if comment.author == request.user or comment.post.author == request.user:
            comment.delete()
            return redirect('comments', comment.post.id)
        else:
            return HttpResponseForbidden('You do not have permission to delete this comment')
        
@login_required
def edit_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)        
    if request.user != comment.author and comment != None:
        return HttpResponseForbidden('You do not have permission to edit this comment')
    
    if request.method == 'GET':
        return render(request, 'Posts/comments.html', {'comment': comment, "post": comment.post, "type": 'Edit'})
    
    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('comments', comment.post.id)
