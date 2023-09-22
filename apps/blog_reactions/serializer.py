from rest_framework.serializers import ModelSerializer
from apps.blog_reactions.models import LikeBlog
from apps.blog.serializer import BlogsSerializers
from apps.user_system.serializer import ModelUserDjoserSerializers


class LikesSerializer (ModelSerializer):
    user = ModelUserDjoserSerializers()
    
    class Meta :
        model = LikeBlog
        fields = ["like", "selected", "blog", "user"]