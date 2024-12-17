from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_events, name='events'),
    path('view/<int:event_id>/', views.get_event, name='view_event'),
    path('create/', views.create_event, name='create_event'),
    path('update/<int:event_id>/', views.update_event, name='update_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('register/<int:event_id>/', views.create_attendee, name='register_event'),
    path('attendee/<int:attendee_id>/', views.get_attendee, name='attendee'),
    path('register/delete/<int:event_id>', views.delete_attendee, name='delete_attendee'),
]
