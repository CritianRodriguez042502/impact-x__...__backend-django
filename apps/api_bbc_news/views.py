from django.http import JsonResponse, HttpResponse
import requests

apiKey = "da09c7a07669433f86613d78bc8721ea";
url = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={apiKey}';


def news (request) :
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
        return JsonResponse(
            {"blogs" : "por categoria"}
        )
    else :
        return HttpResponse(f"El metodo '{request.method}' no esta permitido")