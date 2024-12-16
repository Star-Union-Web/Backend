from django.urls import path
from . import views
from .views import PostDetailView
from users import views as users_views
urlpatterns = [
    path('', views.index, name='blog-home'),
    path('create/', views.create_post, name='create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('create_comment/<int:on>', views.create_comment, name='create_comment'),
    path('readprofile/<int:id>', users_views.read_profile, name='readprofile')
]