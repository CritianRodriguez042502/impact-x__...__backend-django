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



class CommentsBlog (models.Model):
    unique_brand = models.CharField(unique=True, max_length=400)
    comments = models.CharField(max_length=250)
    creation = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    user = models.ForeignKey(Model_users, on_delete=models.CASCADE, null=True)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, null=True)
    
    def __str__(self) :
        return self.comments
    
    def save(self, *args, **kwargs) :
        if not self.unique_brand :
            self.unique_brand = str(self.comments)
        super().save(*args,**kwargs)