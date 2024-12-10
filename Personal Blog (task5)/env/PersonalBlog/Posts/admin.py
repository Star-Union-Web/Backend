from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "author", "is_published"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["content", "created_at", "author", "post"]

admin.site.register(Post, PostAdmin)