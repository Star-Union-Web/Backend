from django.contrib import admin
from .models import Attendee, Event
# Register your models here.

admin.site.register(Event)
admin.site.register(Attendee)