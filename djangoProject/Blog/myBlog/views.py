from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Post
from datetime import datetime
# Create your views here.
def index(request):
    if request.method=='POST':
        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(request,username = username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            messages.success(request,('username or password incorrect, try again ... '))
            return redirect('index')
    else:        
        return render(request,'index.html')

def home(request):
    all = Post.objects.all()
    return render(request,'home.html',{'all':all})



def add(request):
    return render(request,'add.html')


def addrec(request):
    title = request.POST['title']
    slug = request.POST['slug']
    content = request.POST['content']
    author = request.POST['author']
    created_at = request.POST['created_at']
    last_updated = request.POST['last_updated']
    publish_status = request.POST.get('published_status') == 'on'
    ob = Post(title=title,slug=slug,content=content,author=author,created_at=created_at,last_updated=last_updated,published_status=publish_status)
    ob.save()
    return redirect("/home")

def delete(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/home')



def update(request,id):
    post = Post.objects.get(id=id)
    return render(request,'update.html',{'post':post})


def uprec(request,id):
    title = request.POST['title']
    slug = request.POST['slug']
    content = request.POST['content']
    author = request.POST['author']
    created_at = request.POST['created_at']
    last_updated = datetime.now()
    publish_status = request.POST.get('published_status') == 'on'
    ob = Post.objects.get(id=id)
    ob.title=title
    ob.slug=slug
    ob.content=content
    ob.author=author
    ob.created_at=created_at
    ob.last_updated=last_updated
    ob.published_status=publish_status
    ob.save()
    return redirect("/home")