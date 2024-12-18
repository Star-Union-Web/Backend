from django.forms import ModelForm
from django import forms

from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'start_date', 'end_date', 'capacity', 'status']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter event title'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3', 'rows': 4, 'placeholder': 'Enter event description'}),
            'location': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter event location'}),
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control mb-3'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control mb-3'}),
            'organizer': forms.Select(attrs={'class': 'form-select mb-3'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter event capacity'}),
            'status': forms.Select(attrs={'class': 'form-select mb-3'}),
        }
