from rest_framework import permissions,status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser,FormParser
from rest_framework.response import Response

from apps.blog.models import Blogs
from apps.blog_reactions.models import LikeBlog
from apps.user_system.models import Model_users


class Likes (APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser,FormParser]
    
    def patch (self,request,format = None):
        filter_blog = Blogs.objects.get(slug = str(request.data["slug"]))
        user = Model_users.objects.get(id = request.user.id)
        
        try :
            
            blog_user_with_activity = LikeBlog.objects.get(blog = filter_blog.id, user = request.user.id )
            
            if blog_user_with_activity :
                
                if str(request.data["like"]).lower() == "true":
                    blog_user_with_activity.selected = True
                    blog_user_with_activity.like = int(blog_user_with_activity.like) + 1
                    blog_user_with_activity.save()
                    return Response ({"success": "success"}, status=status.HTTP_200_OK)
                
                else :
                    blog_user_with_activity.selected = False
                    blog_user_with_activity.like = int(blog_user_with_activity.like) - 1
                    blog_user_with_activity.save()
                    return Response ({"success": "success"}, status=status.HTTP_200_OK)
                
            else :
                return Response({"error" : "error"}, status=status.HTTP_404_NOT_FOUND)
            
        except :
            
            if str(request.data["like"]).lower() == "true" :
                create_like_for_user = LikeBlog.objects.create(
                    like = 1,
                    selected = True,
                    blog = filter_blog,
                    user = user,
                )
                create_like_for_user.save()
                return Response ({"success": "success"}, status=status.HTTP_200_OK)
            
            else :
                return Response({"error" : "error"}, status=status.HTTP_404_NOT_FOUND)
                
            
            
        
    
        
        
        
        
                
                
        