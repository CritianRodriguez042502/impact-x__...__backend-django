from django.utils.text import slugify
from django.http import JsonResponse


from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser

from apps.blog.models import Blogs, Categoryes
from apps.blog.pagination import MediumPagination
from apps.blog.serializer import BlogsSerializers

from apps.user_system.models import Model_users

from apps.dashboard.utils import generate_random_string

from apps.blog_reactions.models import LikeBlog, CommentsBlog
from apps.blog_reactions.serializer import LikesSerializer, CommentsBlogSerializer

from random import uniform
from decouple import config
import requests


# =============== Isauthenticated user ===============

@api_view(["GET"])
@permission_classes(permission_classes=[permissions.IsAuthenticated])
def getAllUsernames(request):
    filter_usernames = Model_users.objects.all()
    all_usernames = []
    if filter_usernames.exists():
        for data in filter_usernames:
            all_usernames.insert(0, data.username)
        return Response({"data": all_usernames}, status=status.HTTP_200_OK)
    else:
        return Response({"notFound": "NotFound"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@permission_classes(permission_classes=[permissions.IsAuthenticated])
def BlogByUser(request):
    blog_user_list = []
    blogs_user = Blogs.objects.order_by("creation").filter(user=request.user.id)
    blog_user_list.extend(blogs_user)
    blog_user_list.reverse()
    
    if blogs_user:
        
        pagination = MediumPagination()
        response = pagination.paginate_queryset(blog_user_list, request)
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


@api_view(["GET"])
@permission_classes(permission_classes=[permissions.AllowAny])
def getUserBlogReactions(request):
    slug = request.query_params.get("slug")
    filter_blog = Blogs.objects.filter(slug=slug)
    filter_comments = []
    filter_likes = []

    if filter_blog and len(filter_blog) == 1:
        for data in filter_blog:
            likes = LikeBlog.objects.filter(blog=data.id)
            filter_likes.extend(likes)
        for data in filter_blog:
            comments = CommentsBlog.objects.filter(blog=data.id)
            filter_comments.extend(comments)
        
        serializer_likes = LikesSerializer(filter_likes, many=True)
        serializer_comments = CommentsBlogSerializer(
            filter_comments, many=True)

        return Response({
            "likes": serializer_likes.data,
            "comments": serializer_comments.data
        }, status=status.HTTP_200_OK)

    else:
        return Response({"error": "Error"}, status=status.HTTP_409_CONFLICT)

# =============== Create, Update and delete Blogs ===============


@api_view(["POST"])
@permission_classes(permission_classes=[permissions.IsAuthenticated])
@parser_classes(parser_classes=[JSONParser, FormParser, MultiPartParser])
def createBlogUser(request):
    user = request.user
    url_upload_img = config("URL_UPLOAD_IMG")
    key_upload_img = config("KEY_UPLOAD_IMG")
    select_category = Categoryes.objects.get(name=request.data["category"])

    string_random = str(generate_random_string(25)).lower()
    num_random = str(round(uniform(1, 400)))
    backup_slug = slugify(str(user.username) + "slug" + str(request.data["title"]) + string_random + num_random)
    
    public = False
    if str(request.data["public"]).lower() == "true":
        public = True
    else:
        public = False
    
    image = request.data.get("file")
    
    def uploadImg () :
        url = url_upload_img
        
        info = {
            "key" : key_upload_img
        }
        
        if not image :
            return Response({"Error": "No se a proporsionado imagen"}, status=status.HTTP_409_CONFLICT)
        
        res = requests.post(url=url, data=info,files={"image" : image})
        
        if res.status_code == 200 : 
            data = res.json()
            return data["data"]["url"]
        
        if res.status_code != 200 :
            return Response({"Error" : "Ah pasado un error al querer cargar la imagen"},status=409)
    
    new_url_image = uploadImg()
    
    try:
        new_blog = Blogs.objects.create(
            title=request.data["title"],
            description=request.data["description"].capitalize(),
            public=public,
            img_url = new_url_image,
            slug= slugify(str(user.username) + "slug" + str(request.data["title"])),
            content=str(request.data["content"]),
            category=select_category,
            user=user
        )
        new_blog.save()

        try:
            slug_to_select_blog_model = slugify(
                str(user.username) + "slug" + str(request.data["title"]))
            blog_for_like_model = Blogs.objects.get(
                slug=slug_to_select_blog_model)
            new_like_model = LikeBlog.objects.create(
                like=0,
                selected=False,
                blog=blog_for_like_model,
                user=user
            )
            new_like_model.save()
            return Response({"success": "Blog creado"}, status=status.HTTP_201_CREATED)

        except:
            return Response({"error": "Error"}, status=401)

    except:

        try:
            new_blog = Blogs.objects.create(
                title=request.data["title"],
                description=request.data["description"].capitalize(),
                public=public,
                img_url = new_url_image,
                slug=backup_slug,
                content=str(request.data["content"]),
                category=select_category,
                user=user
            )
            new_blog.save()

            try:
                blog_for_like_model = Blogs.objects.get(slug=backup_slug)

                new_like_model = LikeBlog.objects.create(
                    like=0,
                    selected=False,
                    blog=blog_for_like_model,
                    user=user
                )
                new_like_model.save()
                return Response({"success": "Blog creado"}, status=status.HTTP_201_CREATED)

            except:
                return Response({"error": "Error"}, status=402)

        except:
            return Response({"error": "Error"}, status=403)



@api_view(["PUT"])
@permission_classes([permissions.IsAuthenticated])
@parser_classes([JSONParser, FormParser, MultiPartParser])
def updateBlogsByUser(request):
    slug = request.query_params.get("slug")
    user = request.user

    url_upload_img = config("URL_UPLOAD_IMG")
    key_upload_img = config("KEY_UPLOAD_IMG")

    filter_blog_user = Blogs.objects.filter(user=user.id, slug=slug)
    filter_category = Categoryes.objects.get(name=str(request.data["category"]))

    string_random = str(generate_random_string(25)).lower()
    num_random = str(round(uniform(1, 400)))

    if filter_blog_user:
        image = request.data.get("file")
        
        def uploadImg():
            url = url_upload_img
            info = {"key": key_upload_img}
            res = requests.post(url=url, data=info, files={"image": image})

            if res.status_code == 200:
                data = res.json()
                return data["data"]["url"]
            
            return None

        new_url_image = "" 
        
        if image != "undefined" :
            new_url_image = uploadImg() 

        for blog in filter_blog_user:
            blog.title = request.data["title"]
            blog.description = request.data["description"].capitalize()
            blog.content = request.data["content"]

            if str(request.data["public"]).lower() == "true":
                blog.public = True
            else:
                blog.public = False

            if new_url_image:
                try :
                    blog.img_url = new_url_image  
                except : 
                    False

            blog.category = filter_category

            try:
                blog.slug = slugify(str(user.username) + "slug" + str(request.data["title"]))
                blog.save()
                return Response({"success": "update completed"}, status=status.HTTP_200_OK)
            
            except:
                
                try:
                    blog.slug = slugify(str(user.username) + "slug" + str(request.data["title"]) + string_random + num_random)
                    blog.save()
                    return Response({"success": "update completed"}, status=status.HTTP_200_OK)
                
                except:
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
    