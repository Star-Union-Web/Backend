from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #status = models.TextChoices()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



# Create your models here.

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=555)
    date_posted = models.DateTimeField(default=timezone.now)
    posted_on = models.ForeignKey(Post, on_delete=models.CASCADE)