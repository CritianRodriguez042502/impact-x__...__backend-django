from rest_framework import status, exceptions, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models.query_utils import Q
from apps.blog.pagination import MediumPagination, BigPagination
from apps.blog.serializer import CategorySerializers, BlogsSerializers
from apps.blog.models import Categoryes, Blogs
from django.http import HttpResponse,JsonResponse



# All categoryes
class AllCategorys (APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        categoryes = Categoryes.objects.all()

        if categoryes:
            serializer = CategorySerializers(categoryes, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "not_Found"}, status=status.HTTP_404_NOT_FOUND, exception=exceptions.NotFound)



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
            return Response({"Error": "not_Found"}, status=status.HTTP_404_NOT_FOUND, exception=exceptions.NotFound)



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

                else:
                    return Response({"erorr": "not_Found"}, status=status.HTTP_404_NOT_FOUND, exception=exceptions.NotFound)

            else:
                return Response({"erorr": "not_Found"}, status=status.HTTP_404_NOT_FOUND, exception=exceptions.NotFound)

        else:
            return Response({"erorr": "not_Found"}, status=status.HTTP_404_NOT_FOUND, exception=exceptions.NotFound)



class BLogDetail (APIView):
    permission_classes =[permissions.AllowAny]
    
    def get(self, request, format = None):
        if Blogs.objects.all() :
            slug = request.query_params.get("slug")
            blog = Blogs.objects.filter(slug = slug)
            
            if blog:
                seiralizer = BlogsSerializers(blog, many = True)
                return Response(seiralizer.data)
            
            else:
                return Response({"erorr": "not_Found"}, status=status.HTTP_404_NOT_FOUND, exception=exceptions.NotFound)
        
        else:
            return Response({"erorr": "not_Found"}, status=status.HTTP_404_NOT_FOUND, exception=exceptions.NotFound)



class SearchBlogs (APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self,request,format = None):
        
        if Blogs.objects.all():
            slug = request.query_params.get("slug")
            blogs = Blogs.objects.order_by("-creation").filter(Q(title__startswith = slug ), public = True)
            
            if blogs:
                pagination = BigPagination()
                response = pagination.paginate_queryset(blogs, request)
                serializer = BlogsSerializers(response, many = True)
                return pagination.get_paginated_response(serializer.data)
            
            else:
                return Response({"erorr": "not_Found"}, status=status.HTTP_404_NOT_FOUND, exception=exceptions.NotFound)
            
        else:
            return Response({"erorr": "not_Found"}, status=status.HTTP_404_NOT_FOUND, exception=exceptions.NotFound)