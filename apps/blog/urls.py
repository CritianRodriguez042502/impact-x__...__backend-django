from django.urls import path, include
from apps.blog import views


urls_blog = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('all_categoryes/', views.AllCategorys.as_view()),
    path('all_blog/', views.AllBlogs.as_view()),
    path('blog_by_category/', views.BlogsByCategoryView.as_view()),
    path('blog_detail/', views.BLogDetail.as_view()),
    path('search_blogs/', views.SearchBlogs.as_view()),
]

urls_blog_by_user = [
    path('blog_by_user/', views.BlogByUser),
    path('blog_detail_by_user/', views.blogDetailByUser),
    path("create_blog_by_user/", views.createBlogUser),
    path('update_blogs_by_user/', views.updateBlogsByUser),
    path('delete_blog_by_user/', views.DeleteBlogByUser)
]

urlpatterns = urls_blog + urls_blog_by_user
