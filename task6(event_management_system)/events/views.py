
from django.shortcuts import render
from django.http import HttpResponse
from .forms import EventCreationForm
from .models import Attendee, Event
from django.views.generic import ListView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from users.decorators import *

import datetime

# Create your views here.


class HomeListView(ListView):
    template_name = 'home.html'
    context_object_name = 'events'
    model = Event

class EventDetailView(DetailView):
    template_name = 'event_details.html'
    context_object_name = 'event'
    model = Event

    def get_context_data(self, **kwargs):
        event_id = self.kwargs.get('pk')
        print(event_id)
        context = super().get_context_data(**kwargs)
        context['attendee_count'] = Attendee.objects.all().filter(event=Event.objects.all().filter(id=event_id).first()).count()
        return context
@login_required
@allowed_user_types(['organizer'])
def create_event(request):
    form = EventCreationForm()
    if request.method == "POST":
        form = EventCreationForm(request.POST, request.FILES)

        if form.is_valid():
            x = form.save(commit=False)
            x.organizer = request.user
            x.save()
            return redirect('home')
        else:
            form = EventCreationForm()
    
    return render(request, 'create_event.html', {'form': form})


@login_required
@allowed_user_types(['organizer'])
def edit_event(request):
    return HttpResponse("Edit")
@login_required
def register_for_event(request, **kwargs):
    if request.method == 'POST':
        x = kwargs.get('pk')
        reg_event = Event.objects.all().filter(id = x).first()
        if Attendee.objects.all().filter(attendee=request.user, event=reg_event).first():
            return HttpResponse("You are already registered for this event")
        else:
            attendees_number = Attendee.objects.all().filter(event=reg_event).count()
            print(type(reg_event.capacity))
            max_attendees = reg_event.capacity
            if attendees_number < max_attendees:
                attendee_inst = Attendee(attendee=request.user, event=reg_event, reg_date=datetime.datetime.now())
                attendee_inst.save()
                return redirect('event_details', x)
            else:
                return HttpResponse("Sorry, this event is fully occupied :(")
        

        print(request.POST)
    return render(request, 'event_register.html')