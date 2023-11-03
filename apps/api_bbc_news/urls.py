from django.urls import path
from apps.api_bbc_news import views

urlpatterns = [
    path("initial_news/", view=views.news, name="initial_news"),
    path("news_category/", view=views.newsByCategory, name="news_category")
]