from django.contrib import admin
from .models import Post

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'created_at')

admin.site.register(Post, BoardAdmin)
# Register your models here.
