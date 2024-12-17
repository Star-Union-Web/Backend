from django import forms
from .models import Post, Comments

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content',)

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']