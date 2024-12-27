from django.urls import path
from .views import HomeListView, create_event, EventDetailView, register_for_event
urlpatterns = [
    path('home/', HomeListView.as_view(), name='home'),
    path('create/',create_event ),
    path('<int:pk>/', EventDetailView.as_view(), name='event_details'),
    path('register/<int:pk>', register_for_event, name='event_register')
    
]