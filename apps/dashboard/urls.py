from django.urls import path
from apps.dashboard import views


urlpatterns = [
    path('blog_by_user/', views.BlogByUser),
    path('blog_detail_by_user/', views.blogDetailByUser),
    path("create_blog_by_user/", views.createBlogUser),
    path('update_blogs_by_user/', views.updateBlogsByUser),
    path('delete_blog_by_user/', views.DeleteBlogByUser),
]

usernames = [
    path("get_all_usernames/", views.getAllUsernames)
]

likes_and_comment = [
    path('get_user_blog_reactions/', views.getUserBlogReactions)
]

urlpatterns.extend(likes_and_comment)
urlpatterns.extend(usernames)


# Test
