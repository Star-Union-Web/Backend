from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date


# Create your models here.
class user_profile(models.Model):
    status_choices = [('admin','admin'),('author','author'),('reader','reader')]
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=30,choices=status_choices)
    def __str__(self):
        return self.name




class Post(models.Model):
    published_choices = [('draft','draft'),('published','published'),('rejected','rejected')]
    title = models.CharField(max_length=100)
    image = models.ImageField(default='photos/default.jpg',upload_to='photos/%y/%m/%d')
    slug = models.SlugField(max_length=200,blank=True)
    content = models.TextField(max_length=500)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    published_status = models.CharField(max_length=30,choices=published_choices)
    def __str__(self):
        return str(self.title)
    


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


    