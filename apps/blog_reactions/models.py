from django.db import models
from apps.blog.models import Blogs
from apps.user_system.models import Model_users

class LikeBlog (models.Model):
    like = models.IntegerField(default=0)
    selected = models.BooleanField(default=False)
    
    user = models.ForeignKey(Model_users, on_delete=models.CASCADE, null=True)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, null=True)
    
    def __str__ (self) :
        return f"{self.blog}"