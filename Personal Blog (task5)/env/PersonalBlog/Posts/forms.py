from django.forms import ModelForm
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'is_published']
        labels = {
            'title': 'Title',
            'content': 'Content',
            'is_published': 'Publish'  
        }
