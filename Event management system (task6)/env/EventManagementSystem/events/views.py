from django.shortcuts import redirect, render
from .models import Event, Attendee
from .forms import EventForm
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden

# Create your views here.


@permission_required('events.view_events', login_url='login')
def get_events(request): 
    if request.method == 'GET':
        events = Event.objects.filter(status="published").prefetch_related('attendee_set')
        user_events_id = [event.id for event in events if event.attendee_set.filter(user=request.user).exists()]
        return render(request, 'events/events.html', {'events': events, 'user_events_id': user_events_id})

@permission_required('events.view_event', login_url='login')  
def get_event(request, event_id):  # this view is used to get a single event with more details to the organizer
    if request.method == 'GET':
        event = Event.objects.get(pk=event_id)
        if event.organizer == request.user or request.user.has_perm('events.admin'):
            attendees = Attendee.objects.filter(event=event)
            [attendee.id for attendee in attendees]
            return render(request, 'events/event_preview.html', {'event': event, 'attendees': attendees})

        if event.status == 'published':
            return render(request, 'events/event_preview.html', {'event': event})

        return HttpResponseForbidden("You are not allowed to view this event")

@permission_required('events.add_event')
def create_event(request):  # this view is used to create a new event by organizers
    form = EventForm()
    if request.method == 'GET':
        return render(request, 'events/create_event.html', {'form': form})
    
    if request.method == 'POST':
        form = EventForm(request.POST)
        form.instance.organizer = request.user
        if form.is_valid():
            form.save()
            return redirect('events')
        else:
            return render(request, 'events/create_event.html', {'form': form})

@permission_required('events.change_event')
def update_event(request, event_id):  # this view is used to update an event by organizers created this event
    event = Event.objects.get(pk=event_id)

    if request.user != event.organizer and not request.user.has_perm('events.admin'):
        return HttpResponseForbidden("You are not allowed to update this event")
    
    form = EventForm(instance=event)

    if request.method == 'GET':
        return render(request, 'events/create_event.html', {'form': form})
    
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events')
        
        return render(request, 'events/create_event.html', {'form': form})

@permission_required('events.delete_event')
def delete_event(request, event_id):  # this view is used to delete an event by organizers created this event
    event = Event.objects.get(pk=event_id)
    if request.user == event.organizer or request.user.has_perm('events.admin'):
        event.delete()
        return redirect('events')
        
    return HttpResponseForbidden("You are not allowed to delete this event")

@permission_required('events.view_attendee')
def get_attendee(request, attendee_id):  # this view is used to view an attendee by the organizer
    attendee = Attendee.objects.get(pk=attendee_id)
    if request.user != attendee.event.organizer and not request.user.has_perm('events.admin'):
        return HttpResponseForbidden("You are not allowed to view this attendee")
    
    attendee = attendee.user
    return render(request, 'events/attendee.html', {'attendee': attendee})

@permission_required('events.add_attendee')
def create_attendee(request, event_id):  # this view is used to register for an event
    if request.method == 'POST':
        event = Event.objects.get(pk=event_id)
        if Attendee.objects.filter(user=request.user, event=event).exists():
            return HttpResponseForbidden("You are already registered for this event")
        if event.status != 'published':
            return HttpResponseForbidden("You are not allowed to register for this event")
        if event.capacity == 0:
            return redirect('events')
        event.capacity -= 1
        event.save()
        attend = Attendee(user=request.user, event=event)
        attend.save()
        return redirect('events')
    
@permission_required('events.delete_attendee')
def delete_attendee(request, event_id):  # this view is used to remove an attendee from an event
    if request.method == 'POST':
        event = Event.objects.get(pk=event_id)
        attendee = Attendee.objects.get(user=request.user, event=event)
        if not attendee:
            return HttpResponseForbidden("You are not registered for this event")
        if attendee or request.user.has_perm('events.admin'):
            event.capacity += 1
            event.save()
            attendee.delete()
            return redirect('events')
        
        return HttpResponseForbidden("You are not allowed to remove this attendee")

