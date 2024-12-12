from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, default="title")
    slug = models.URLField(default="url.com")
    content = models.TextField(max_length="2000", default="content")
    author = models.CharField(max_length=200, default="author")
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    published_status = models.BooleanField()
