from django.urls import path
from .views import HomeListView, create_event, EventDetailView, edit_event, register_for_event, delete_event, my_events
urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('create/',create_event ),
    path('edit/<int:pk>', edit_event, name='edit_event'),
    path('<int:pk>/', EventDetailView.as_view(), name='event_details'),
    path('register/<int:pk>', register_for_event, name='event_register'),
    path('delete/<int:pk>', delete_event, name='delete_event'),
    path('my/', my_events, name='my_events')
    
]