from django.db import models
from Users.models import CustomUser

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    organizer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    capacity = models.IntegerField()
    choices = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('cancelled', 'Cancelled'),
        ('ended', 'Ended')
    )
    status = models.CharField(max_length=32, choices=choices, default='draft')
    
    def __str__(self):
        return self.title
    
class Attendee(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} Registered at {self.date.date()}'    
