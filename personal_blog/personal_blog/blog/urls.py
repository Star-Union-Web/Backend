from django.urls import path
from . import views
from .views import PostDetailView
from users import views as users_views
urlpatterns = [
    #path('', views.index, name='blog-home'),
    path('', views.PostsView.as_view(), name='blog-home'),
    path('create/', views.create_post, name='create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('create_comment/<int:on>', views.create_comment, name='create_comment'),
    path('readprofile/<int:id>', users_views.read_profile, name='readprofile'),
    path('delete_comment/<int:id>', views.delete_comment, name='delete_comment'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post'),
    path('update_post/<int:pk>', views.PostEditView.as_view(), name='update_post'),
]