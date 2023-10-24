from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework import permissions, status
from rest_framework.parsers import FormParser, MultiPartParser

from apps.user_system.models import Model_users

from decouple import config
import requests

@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
@parser_classes([FormParser, MultiPartParser])
def userProfilePicture (request) :
    users = Model_users.objects.all()
    url_upload_img = config("URL_UPLOAD_IMG")
    key_upload_img = config("KEY_UPLOAD_IMG")
    
    if users.exists() :
        
        filter_user = Model_users.objects.filter(id = request.user.id)
        if len(filter_user) == 1 :
            img = request.data.get("file")
            if not img :
                return Response("No se proporciono imagen", status=400)
            
            info = {
                "key" : key_upload_img
            }
            
            res = requests.post(url=url_upload_img, data=info, files={"image" : img})
            url_image = ""
            
            if res.status_code == 200 :
                response_data = res.json()
                url_image = response_data["data"]["url"]
                
                for data in filter_user :
                    data.img_url = url_image
                    data.save()
                    return Response({"Success" : "Success"}, status=status.HTTP_200_OK)
                
            if res.status_code != 200 :
                return Response({"Error" : "no se pudo cargar la imagen"}, status=409)
            
        else :
            return Response({"Error" : "Error"}, status=status.HTTP_409_CONFLICT)
  
        