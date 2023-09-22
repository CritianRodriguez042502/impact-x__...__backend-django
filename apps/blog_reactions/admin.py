from django.contrib import admin
from apps.blog_reactions.models import LikeBlog

# Register your models here.

@admin.register(LikeBlog)
class likesBlogAdmin (admin.ModelAdmin):
    list_display = ["id", "blog","user","selected","like"]