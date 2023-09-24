from django.contrib import admin
from apps.blog_reactions.models import LikeBlog, CommentsBlog

# Register your models here.

@admin.register(LikeBlog)
class LikesBlogAdmin (admin.ModelAdmin):
    list_display = ["id", "blog","user","selected","like"]
    
@admin.register(CommentsBlog)
class CommentsBlogAdmin (admin.ModelAdmin):
    list_display = ["comments", "update", "creation", "blog", "user"]
    