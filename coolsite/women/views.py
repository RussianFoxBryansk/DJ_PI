# для хранения представлений текущего приложения
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("<a href=cod/>Страницу приложения видно 1</a><br><a href=cot/>Страницу приложения видно 2</a>")

def categories(request, cats_id):
    return HttpResponse(f"<h1>Статья под номером {cats_id}</h1>")
def categories_slug(request, cats):
    return HttpResponse(f"<h1>Статья под категории {cats}</h1>")

def moon(request):
    return HttpResponse("<h2> Это же МАРРИО- </h2>")
def moon1(request):
    return HttpResponse("Кот")
def moon2(request):
    return HttpResponse("<img src=https://dobrovserdce.ru/images/2022/11/02/kot%20Fedya_large.jpeg /img>")
