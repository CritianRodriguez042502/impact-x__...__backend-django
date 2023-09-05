from django.contrib import admin
from apps.blog.models import Categoryes,Blogs


@admin.register(Categoryes)
class CategoryesAdmin (admin.ModelAdmin):
    list_display = ["name", "creation"]


@admin.register(Blogs)
class BlogsAdmin (admin.ModelAdmin):
    list_display = ["title", "creation", "public"]
