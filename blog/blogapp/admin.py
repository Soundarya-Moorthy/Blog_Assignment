from django.contrib import admin
from .models import BlogPost
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image')
admin.site.register(BlogPost)
