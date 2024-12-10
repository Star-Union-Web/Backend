from django.urls import path
from . import views

urlpatterns = [
    path("", views.post, name="posts"),
    path("create/", views.create_post, name="create_post"),
    path("edit/<int:post_id>/", views.edit_post, name="edit_post"),
    path("delete/<int:post_id>", views.delete_post, name="delete_post"),
    path("<slug:slug>/", views.view_post, name="view_post"),
    path("edit/<int:post_id>/", views.edit_post, name="edit_post"),
]