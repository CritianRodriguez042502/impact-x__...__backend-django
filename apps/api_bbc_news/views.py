from django.http import JsonResponse, HttpResponse
from datetime import datetime
import requests

apiKey = "da09c7a07669433f86613d78bc8721ea"

def news (request) :
    url = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={apiKey}'
    
    if request.method == "GET":
        res = requests.get(url=url)
        
        if res.status_code == 200 :
            return JsonResponse({"data" : res.json().get("articles")})
        else :
            return HttpResponse("Error")
        
    else :
        return HttpResponse(f"El metodo '{request.method}' no esta permitido")


def newsByCategory (request) :
    if request.method == "GET":
        
        params = request.GET.get("slug")
        
        date_year = 0
        date_month = 0
        date_day = datetime.now().day
        
        if int(datetime.now().month) == 1 :
            date_year = int(datetime.now().year - 1)
            date_month = 12
        else :
            date_year = int(datetime.now().year)
            date_month = int(datetime.now().month - 1)
        
        date_api = f"{date_year}-{int(date_month)}-{date_day}"
        
        url = f'https://newsapi.org/v2/everything?q=${params}&language=es&from={date_api}&sortBy=publishedAt&apiKey={apiKey}'
        
        res = requests.get(url=url)
        
        if res.status_code == 200 and params :
            return JsonResponse({"data" : res.json().get("articles")})
        
        else :
            return JsonResponse({"Error" : str(409)})
    else :
        return HttpResponse(f"El metodo '{request.method}' no esta permitido")