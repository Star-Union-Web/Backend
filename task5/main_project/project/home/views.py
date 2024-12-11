from django.shortcuts import render,redirect, get_object_or_404,HttpResponseRedirect
from .models import *
from .forms import add_data,Register_form,CommentForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout  #login
from django.contrib.auth.decorators import login_required  #for login restriction
# Create your views here.
def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username = request.POST.get("username")
            password = request.POST.get("password")   
            user = authenticate(request ,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            
            else:
                messages.info(request, "this account doesnt exist")
                return redirect('login')
                
            
            
        return render(request ,'pages/login.html')



@login_required(login_url='login')
def home(request):
    posts = Post.objects.all()
    posts = {'posts':posts}
    return render(request,'pages/home.html',posts)

@login_required(login_url='login')
def detailed_page(request,post_id):
    post = get_object_or_404(Post, id=post_id) 
    
    comments = Comment.objects.filter(post=post).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('body')
            comment = Comment.objects.create(post=post , name=request.user.username,body=content)
            comment.save()
            return redirect('detailed_page', post_id=post.id)
    else:
        comment_form = CommentForm()

    return render(request, 'pages/detailed_page.html', {'post': post, 'comments': comments ,'comment_form':comment_form})
    
    
@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')  

        form = add_data(data=request.POST, files=request.FILES)

        if form.is_valid():
            title = request.POST.get('title')
            image = request.FILES.get('image')
            slug = request.POST.get('slug')
            content = request.POST.get('content')
            published_status = request.POST.get('published_status')

            
            author = request.user  
            
            
            post = Post.objects.create(title=title,author=author, content=content, image=image, slug=slug,published_status=published_status)
            post.save()
            return redirect('create')
    else:
        form = add_data()

    return render(request, 'pages/create.html', {'form': form})




def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = Register_form()
    if request.method=='POST':
        form=(Register_form(request.POST))
        if form.is_valid():
            form.save()
            messages.success(request,"account was created for " +  form.cleaned_data.get('username'))  #flash message
            

           
    context = {'data': form}

    return render(request,'pages/register.html' ,context)


@login_required(login_url='login')
def categories (request):
    all_posts = Post.objects.all()
    if request.method=='GET':
        if 'search' in request.GET:
            searchans = request.GET['search']
            if searchans:
                all_posts=all_posts.filter(title__icontains=searchans)

        context = {'data' : all_posts}

    return render(request,'pages/categories.html',context)


@login_required(login_url='login')
def status_filter(request):
    post_type = request.GET.get('search1')

    
    if post_type:
        posts = Post.objects.all().filter(published_status=post_type)
    
    else :
        posts = Post.objects.all() 
   

    return render(request, 'pages/categories.html', {'data': posts})


def Logout (request):
    logout(request)
    return redirect("login")

@login_required(login_url='login')
def update(request, post_id):
    
    post = get_object_or_404(Post, id=post_id)

    
    if request.method == 'POST':
        form = add_data(request.POST, request.FILES, instance=post)  # put the instance to update if it wasnt put it will create a new one
        
        if form.is_valid():
            
            post = form.save(commit=False)
            post.author = User.objects.get(username=request.user.username)  
            post.save()
            return redirect('detailed_page', post_id=post.id) 

    
    else:
        form = add_data(instance=post)  

    return render(request, 'pages/update.html', {'form': form})

@login_required(login_url='login')
def delete(request,post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        post.delete()
    
    return redirect('home')
    