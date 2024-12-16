from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .models import Post, Comments
from .forms import NewPostForm, NewCommentForm
from django.http import HttpResponse
# Create your views here.
#blogs = ["aaaaaaaaaaaaaaaaa", "aaaa", "aaaaaaaaaaaaaaaaaaaa"]

def index(request):
    blogs = Post.objects.all()
    return render(request, 'index.html', {'blogs': blogs})

@login_required
def create_post(request):
    posts = Post()
    form = NewPostForm()
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(request.user)
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('blog-home')
        else:
            form = NewPostForm(instance=request.post)
        
    return render(request, 'create.html', {'form': form})

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(self.request.path[6:])
        #print(self.object.id)
        context['comments'] = Comments.objects.all().filter(posted_on=self.object.id)
        context['comment_form'] = NewCommentForm()
        #print(context['comments'])
        return context
@login_required
def create_comment(request, **kwargs):
    #form = NewCommentForm()
    posted_on = kwargs.get('on')
    if request.method == 'POST':
        form=NewCommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.posted_on = Post.objects.all().filter(id=posted_on).first()
            #print(f"Posted On: {kwargs.get('on')}")
            comment.save()
            print(request.path)
            return redirect('post-detail', posted_on)
    return redirect('post-detail', posted_on)