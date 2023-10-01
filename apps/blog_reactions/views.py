from rest_framework import permissions,status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser,FormParser
from rest_framework.response import Response

from apps.blog.models import Blogs
from apps.blog_reactions.models import LikeBlog
from apps.blog_reactions.models import CommentsBlog
from apps.user_system.models import Model_users

from apps.dashboard.utils import generate_random_string

from django.utils.text import slugify
from random import uniform



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
                
                

class Comments (APIView) :
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser, FormParser]
    
    # Get Detailed blog comment
    def get (self, request, format = None) :
        unique_brand = request.query_params.get("unique_brand")
        filter_comment_blog = CommentsBlog.objects.filter(unique_brand = unique_brand, user = request.user.id)
        
        if filter_comment_blog and len(filter_comment_blog) == 1 :
            for data in filter_comment_blog :
                return Response ({"comment" : data.comments}, status=status.HTTP_200_OK)
        else :
            return Response ({"Error" : "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    
    
    def post (self,request,format = None) :
        user = Model_users.objects.get(id = request.user.id)
        unique_key = slugify(str(request.user.username) + str(request.data["content"]) + str(generate_random_string(35)) + str(round(uniform(1,350))))
        
        try :
            filter_blog = Blogs.objects.get(slug = request.data["slug"])
            new_comment = CommentsBlog.objects.create(
                comments = str(request.data["content"]),
                unique_brand = unique_key,
                blog = filter_blog,
                user = user
            )
            new_comment.save()
            return Response ({"success": "success"}, status=status.HTTP_200_OK)
        
        except :  
            return Response({"error" : "error"}, status=status.HTTP_409_CONFLICT)
    
    
    def patch (self, request, format = None) :
        unique_key = request.data["unique_key"]
        filter_comment = CommentsBlog.objects.filter(unique_brand = unique_key)
        unique_brand = slugify(str(request.user.username) + str(request.data["content"]) + str(generate_random_string(35)) + str(round(uniform(1,350))))
        
        if filter_comment and len(filter_comment) == 1 :
            
            for data in filter_comment :
                data.comments = request.data["content"]
                data.unique_brand = unique_brand
                data.save()
            return Response({"Success" : "Success"}, status=status.HTTP_200_OK)
        
        else :
            
           return Response({"error" : "Parece que hay problemas de inconsistencia"}, status=status.HTTP_409_CONFLICT)
    
    
    def delete(self,request, format = None) :
        unique_key = request.query_params.get("unique_key")
        filter_comment = CommentsBlog.objects.filter(unique_brand = unique_key)
        
        if filter_comment and len(filter_comment) == 1 :
            filter_comment.delete()
            return Response({"success" : "success"}, status=status.HTTP_200_OK)
    
        else :
           return Response({"error" : "Parece que hay problemas de inconsistencia"}, status=status.HTTP_409_CONFLICT)