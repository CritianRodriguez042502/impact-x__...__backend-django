from rest_framework.views import APIView
from rest_framework.decorators import api_view,permission_classes,parser_classes
from rest_framework import status, exceptions, permissions
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.db.models.query_utils import Q

from apps.blog.pagination import SmallPagination,MediumPagination, BigPagination
from apps.blog.serializer import CategorySerializers, BlogsSerializers
from apps.blog.models import Categoryes, Blogs
from apps.user_system.models import Model_users



# All categoryes
class AllCategorys (APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        categoryes = Categoryes.objects.all()
        if categoryes:
            serializer = CategorySerializers(categoryes, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "not_Found"}, status=status.HTTP_404_NOT_FOUND)



# all blogs
class AllBlogs (APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):

        if Blogs.objects.order_by("-creation").all():
            filter_blogs = Blogs.objects.filter(public=True)
            pagination = MediumPagination()
            response = pagination.paginate_queryset(filter_blogs, request)
            serializer = BlogsSerializers(response, many=True)
            return pagination.get_paginated_response(serializer.data)
        else:
            return Response({"Error": "not_Found"}, status=status.HTTP_404_NOT_FOUND)



# Blogs by category view
class BlogsByCategoryView (APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        categorys = Categoryes.objects.all()
        if categorys:
            slug = request.query_params.get("slug")
            filter_category = Categoryes.objects.filter(slug=slug)
            if filter_category:
                blogs = []
                for data in filter_category:
                    blogs.extend(Blogs.objects.filter(
                        category=data.id, public=True))
                
                if blogs:
                    pagination = MediumPagination()
                    response = pagination.paginate_queryset(blogs, request)
                    serializer = BlogsSerializers(response, many=True)
                    return pagination.get_paginated_response(serializer.data)

                else :
                    return Response({"erorr": "not_Found"}, status=status.HTTP_404_NOT_FOUND)

            else :
                return Response({"erorr": "not_Found"}, status=status.HTTP_404_NOT_FOUND)

        else :
            return Response({"erorr": "not_Found"}, status=status.HTTP_404_NOT_FOUND)



class BLogDetail (APIView):
    permission_classes =[permissions.AllowAny]
    
    def get(self, request, format = None):
        if Blogs.objects.all() :
            slug = request.query_params.get("slug")
            blog = Blogs.objects.filter(slug = slug)
            
            if blog:
                seiralizer = BlogsSerializers(blog, many = True)
                return Response(seiralizer.data)
            
            else :
                return Response({"erorr": "not_Found"}, status=status.HTTP_404_NOT_FOUND)
        
        else :
            return Response({"erorr": "not_Found"}, status=status.HTTP_404_NOT_FOUND)



class SearchBlogs (APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self,request,format = None):
        
        if Blogs.objects.all():
            slug = request.query_params.get("slug")
            blogs = Blogs.objects.order_by("-creation").filter(Q(title__startswith = slug ), public = True)
            
            if blogs :
                pagination = BigPagination()
                response = pagination.paginate_queryset(blogs, request)
                serializer = BlogsSerializers(response, many = True)
                return pagination.get_paginated_response(serializer.data)
            
            else :
                return Response({"erorr": "not_Found"}, status=status.HTTP_404_NOT_FOUND)
            
        else :
            return Response({"erorr": "not_Found"}, status=status.HTTP_404_NOT_FOUND)



# Blogs of users

@api_view(["GET"])
@permission_classes(permission_classes=[permissions.IsAuthenticated])
def BlogByUser (request) : 
    blogs_user = Blogs.objects.order_by("-creation").filter(user = request.user.id, public = True)
    if blogs_user :
        pagination = SmallPagination()
        response = pagination.paginate_queryset(blogs_user, request)
        serializer = BlogsSerializers(response, many = True)
        return pagination.get_paginated_response(serializer.data)
     
    else : 
        return Response ({"not_Found" : "404"}, status=status.HTTP_404_NOT_FOUND)
    
    

@api_view(["GET"])
@permission_classes(permission_classes=[permissions.IsAuthenticated])
def blogDetailByUser (request) :
    slug = request.query_params.get("slug")
    filter_blog_user = Blogs.objects.filter(user = request.user.id, slug = slug)
    if filter_blog_user:
        serializer = BlogsSerializers(filter_blog_user, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    else :
        return Response({"Error" : "not_Found"}, status=status.HTTP_404_NOT_FOUND)


#############

@api_view(["PUT"])
@permission_classes(permission_classes=[permissions.IsAuthenticated])
@parser_classes(parser_classes=[JSONParser])
def updateBlogsByUser (request):
    slug = request.query_params.get("slug")
    filter_blog_user = Blogs.objects.filter(user = request.user.id, slug = slug)
    if filter_blog_user :
        for blog in filter_blog_user :
            blog.title = request.data["title"]
            blog.slug = "slug_" + str(request.data["title"]) + "_" + str(request.user)
            blog.description = request.data["description"].capitalize()
            public = str(request.data["public"]).capitalize()
            if public == "True":
                blog.public = True
            else :
                blog.public = False
            blog.save()
            return Response ({"success" : "update completed"}, status=status.HTTP_200_OK)
        
    else :
        return Response({"Error" : "not_Found"}, status=status.HTTP_404_NOT_FOUND)


