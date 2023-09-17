from django.utils.text import slugify

from rest_framework.decorators import api_view,permission_classes,parser_classes
from rest_framework import permissions,status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,FormParser,FileUploadParser

from apps.blog.models import Blogs,Categoryes
from apps.blog.pagination import MediumPagination
from apps.blog.serializer import BlogsSerializers

from apps.dashboard.utils import generate_random_string

from random import uniform

# =============== Isauthenticated user ===============

@api_view(["GET"])
@permission_classes(permission_classes=[permissions.IsAuthenticated])
def BlogByUser(request):
    blogs_user = Blogs.objects.order_by("-update").filter(user=request.user.id)
    if blogs_user:
        pagination = MediumPagination()
        response = pagination.paginate_queryset(blogs_user, request)
        serializer = BlogsSerializers(response, many=True)
        return pagination.get_paginated_response(serializer.data)

    else:
        return Response({"not_Found": "404"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@permission_classes(permission_classes=[permissions.IsAuthenticated])
def blogDetailByUser(request):
    slug = request.query_params.get("slug")
    filter_blog_user = Blogs.objects.filter(user=request.user.id, slug=slug)
    if filter_blog_user:
        serializer = BlogsSerializers(filter_blog_user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    else:
        return Response({"Error": "not_Found"}, status=status.HTTP_404_NOT_FOUND)



# =============== Create, Update and delete Blogs ===============

@api_view(["POST"])
@permission_classes(permission_classes=[permissions.IsAuthenticated])
@parser_classes(parser_classes=[JSONParser, FormParser, FileUploadParser])
def createBlogUser(request):
    user = request.user
    select_category = Categoryes.objects.get(name = request.data["category"])
    
    string_random = str(generate_random_string(25)).lower()
    num_random = str(round(uniform(1,400)))
     
    public = False    
    if str(request.data["public"]).lower() == "true" :
        public = True
    else :
        public = False
    
    try :
        new_blog = Blogs.objects.create(
            title = request.data["title"],
            description = request.data["description"].capitalize(),
            public = public,
            slug = slugify(str(user.username) + "slug" + str(request.data["title"])),
            content = str(request.data["content"]),
            category = select_category,
            user = user
        )
        new_blog.save()
        return Response({"success": "Blog creado"}, status=status.HTTP_201_CREATED)
    except :
        try :
            new_blog = Blogs.objects.create(
                title = request.data["title"],
                description = request.data["description"].capitalize(),
                public = public,
                slug = slugify(str(user.username) + "slug" + str(request.data["title"]) + string_random + num_random),
                content = str(request.data["content"]),
                category = select_category,
                user = user
            )
            new_blog.save()
            return Response({"success": "Blog creado"}, status=status.HTTP_201_CREATED)
        except :
            return Response ({"error" : "Error"}, status=status.HTTP_409_CONFLICT)
    
    
        
@api_view(["PUT"])
@permission_classes(permission_classes=[permissions.IsAuthenticated])
@parser_classes(parser_classes=[JSONParser])
def updateBlogsByUser(request):
    slug = request.query_params.get("slug")
    user = request.user
    filter_blog_user = Blogs.objects.filter(user = user.id, slug = slug)
    filter_category = Categoryes.objects.get(name = str(request.data["category"]))
    
    string_random = str(generate_random_string(25)).lower()
    num_random = str(round(uniform(1,400)))
           
    if filter_blog_user:
        for blog in filter_blog_user:
            
            blog.title = request.data["title"]
            blog.description = request.data["description"].capitalize()
            blog.content = request.data["content"]
            
            if str(request.data["public"]).lower() == "true" :
                blog.public = True
            else :
                blog.public = False
            
            blog.category = filter_category
            
            try:
                blog.slug = slugify(str(user.username) + "slug" + str(request.data["title"]))
                blog.save()
                return Response({"success": "update completed"}, status=status.HTTP_200_OK)
            
            except :
                try :
                    blog.slug = slugify(str(user.username) + "slug" + str(request.data["title"]) + string_random + num_random )
                    blog.save()
                    return Response({"success": "update completed"}, status=status.HTTP_200_OK)
                except :
                    return Response({"Error": "Conflict"}, status=status.HTTP_409_CONFLICT)
    else:
        return Response({"Error": "not_Found"}, status=status.HTTP_404_NOT_FOUND)



@api_view(["DELETE"])
@permission_classes(permission_classes=[permissions.IsAuthenticated])
def DeleteBlogByUser(request):
    slug = request.query_params.get("slug")
    filter_blog = Blogs.objects.filter(slug=slug)
    if len(filter_blog) != 0:
        filter_blog.delete()
        return Response({"success": "Blog eliminado correctamente"}, status=status.HTTP_202_ACCEPTED)
    else:
        return Response({"Error": "Error"}, status=status.HTTP_403_FORBIDDEN)