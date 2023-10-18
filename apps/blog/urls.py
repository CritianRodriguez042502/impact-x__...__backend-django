from django.urls import path, include
from apps.blog import views

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('all_categoryes/', views.AllCategorys.as_view()),
    path('all_blog/', views.AllBlogs.as_view()),
    path('blog_by_category/', views.BlogsByCategoryView.as_view()),
    path('blog_detail/', views.BLogDetail.as_view()),
    path("get_blog_likes/", views.GetBlogLikes.as_view()),
    path('get_blog_comments/', views.GetBlogComments.as_view()),
    path('search_blogs/', views.SearchBlogs.as_view()),
    path('create/', views.CreateCategorys.as_view()),
]