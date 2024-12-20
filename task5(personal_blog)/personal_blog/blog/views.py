from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView, ListView
from .models import Post, Comments
from .forms import NewPostForm, NewCommentForm, EditPostForm
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
#blogs = ["aaaaaaaaaaaaaaaaa", "aaaa", "aaaaaaaaaaaaaaaaaaaa"]


class PostsView(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "blogs"
    ordering = ['-date_posted']
    paginate_by = 5



#def index(request):
#    blogs = Post.objects.all()
#    return render(request, 'index.html', {'blogs': blogs})

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
    # add additional context by overwriting get_context_data()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(self.request.path[6:])
        #print(self.object.id)
        context['comments'] = Comments.objects.all().filter(posted_on=self.object.id)
        context['comment_form'] = NewCommentForm()
        #print(context['comments'])
        return context

class PostEditView(UpdateView):
    model = Post
    template_name='post_edit.html'
    fields = ['title', 'content']
    #success_url = reverse('blog-detail')
    #success_url = redirect('blog-detail')
    #def get_context_data(self, **kwargs):
     #   context = super().get_context_data(**kwargs)
      #  context['form'] = EditPostForm()
       # return context

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

def update_comment(request, **kwargs):
    return HttpResponse("🫵")

@login_required
def delete_comment(request, **kwargs):
    comment_id = kwargs.get('id')
    comment = Comments.objects.all().filter(id = comment_id).first()
    #print(comment.first())
    comment_author = comment.author
    if request.user.id == User.objects.all().filter(id = comment_author.id).first().id:
        comment.delete()
        return redirect('profile')
    else:
        return HttpResponse("Invalid Comment")
    


@login_required
def delete_post(request, **kwargs):
    post_id = kwargs.get('id')
    post = Post.objects.all().filter(id = post_id).first()
    #print(comment.first())
    post_author = post.author
    if request.user.id == User.objects.all().filter(id = post_author.id).first().id:
        post.delete()
        return redirect('profile')
    else:
        return HttpResponse("Invalid Post")