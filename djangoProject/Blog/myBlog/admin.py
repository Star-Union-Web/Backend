from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = "title","slug","content","author","created_at","last_updated","published_status"

admin.site.register(Post,PostAdmin)