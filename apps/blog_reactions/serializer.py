from rest_framework.serializers import ModelSerializer
from apps.blog_reactions.models import LikeBlog, CommentsBlog
from apps.user_system.serializer import ModelUserDjoserSerializers


class LikesSerializer (ModelSerializer):
    user = ModelUserDjoserSerializers()
    
    class Meta :
        model = LikeBlog
        fields = ["id","like", "selected", "blog", "user"]
    

class CommentsBlogSerializer (ModelSerializer) :
    user = ModelUserDjoserSerializers()
    
    class Meta :
        model = CommentsBlog
        fields = ["id","comments", "creation", "update", "unique_brand", "blog", "user"]