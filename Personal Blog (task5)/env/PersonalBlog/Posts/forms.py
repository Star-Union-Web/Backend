from django.forms import ModelForm
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'is_published']
        labels = {
            'title': 'Title',
            'content': 'Content',
            'slug': 'URL',
            'is_published': 'Publish'  
        }
