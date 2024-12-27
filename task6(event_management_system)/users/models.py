from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = User
    image = models.ImageField(default='default_pfp.png', upload_to='profile_pics')
    email = models.EmailField(unique=True)

    
