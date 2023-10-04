from django.urls import path, include
from apps.user_system import views

urlpatterns = [
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/", include('djoser.social.urls')),
]

uploadImg = [
    path("upload_img_user/", views.userProfilePicture, name="uploadImg"),
]

urlpatterns += uploadImg