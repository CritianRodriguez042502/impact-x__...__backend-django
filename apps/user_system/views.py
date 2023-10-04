from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework import permissions, status
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser

from apps.user_system.models import Model_users

@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
@parser_classes([FormParser, MultiPartParser])
def userProfilePicture (request) :
    users = Model_users.objects.all()
    
    if users.exists() :

        try :
            filter_user = Model_users.objects.get(id = request.user.id)
            filter_user.img = request.FILES["file"]
            filter_user.save()
            return Response({"Success" : "Success"}, status=status.HTTP_200_OK)
    
        except :
            return Response({"Error" : "Error"}, status=status.HTTP_409_CONFLICT)
        
    
@api_view(["PUT"])
@permission_classes([permissions.IsAuthenticated])
@parser_classes([FormParser,MultiPartParser])
def updateBlogImage (request) :
    return Response("Bien")