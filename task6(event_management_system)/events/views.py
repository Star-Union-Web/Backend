
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .forms import EventCreationForm, EventEditForm
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



#class EventEditView(UpdateView):
#    template_name='edit_event.html'
#    model = Event
#    fields = ['title', 'description', 'location', 'start_date', 'end_date', 'image', 'capacity']
@login_required
@allowed_user_types(['organizer'])
def my_events(request):
    events = Event.objects.all().filter(organizer=request.user)
    return render(request, 'my_events.html', {'events': events})
    

@login_required
@allowed_user_types(['organizer'])
def edit_event(request, **kwargs):
    context = {}
    event_id = kwargs.get('pk')
    event = Event.objects.all().filter(id=event_id)[0]
    form = EventEditForm(instance=event)
    if request.method == 'POST':
        form = EventEditForm(request.POST, request.FILES)
        
        if form.is_valid():
            if request.user.username == event.organizer.username:

                x = form.save(commit=False)
                x.organizer=request.user
                event.title = x.title
                event.description = x.description
                event.start_date = x.start_date
                event.end_date = x.end_date
                event.location = x.location
                event.capacity = x.capacity

                event.save()
                return redirect('event_details', event_id)
            else:
                return HttpResponse("you can't edit this event")
    return render(request, 'edit_event.html', {'form': form})

@login_required
@allowed_user_types(['organizer'])
def delete_event(request, **kwargs):
    event_id = kwargs.get('pk')
    event = Event.objects.all().filter(id=event_id)[0]

    if request.user.username == event.organizer.username:
        event.delete()
        #event.save()
    return redirect('my_events')
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