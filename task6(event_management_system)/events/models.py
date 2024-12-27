#from email.mime import image
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    capacity = models.IntegerField()
    #status = models.TextChoices()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='event_pics')

class Attendee(models.Model):
    attendee = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    reg_date = models.DateTimeField()

