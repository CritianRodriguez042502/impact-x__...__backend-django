"""
URL configuration for agency_server project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from django.http import JsonResponse

def home (request):
    return JsonResponse({"welcome" : "Server" })

urlpatterns = [
    path('', home, name ="home"),
    path('admin/', admin.site.urls),
    path("user_system/", include("apps.user_system.urls")),
    path('blog/',include("apps.blog.urls")),
    path("blog_reactions/", include("apps.blog_reactions.urls")),
    path("dashboard/", include("apps.dashboard.urls")),
    path("news/", include("apps.api_bbc_news.urls"))
] 
urlpatterns.extend(static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT))
