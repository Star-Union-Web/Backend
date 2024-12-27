from dataclasses import fields
from django import forms
from .models import Event, Attendee

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'start_date', 'end_date', 'capacity', 'image']
    

class EventEditForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'start_date', 'end_date', 'capacity', 'image']


