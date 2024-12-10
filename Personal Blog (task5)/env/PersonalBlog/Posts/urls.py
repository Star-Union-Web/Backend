from django.urls import path
from . import views

urlpatterns = [
    path("", views.post, name="posts"),
    path("create/", views.create_post, name="create_post"),
    path("edit/<int:post_id>/", views.edit_post, name="edit_post"),
    path("delete/<int:post_id>", views.delete_post, name="delete_post"),
    path("edit/<int:post_id>/", views.edit_post, name="edit_post"),
    path("comments/<int:post_id>/", views.comments, name="comments"),
    path("comments/delete/<int:comment_id>/", views.delete_comment, name="delete_comment"),
    path("comments/edit/<int:comment_id>/", views.edit_comment, name="edit_comment"),
]