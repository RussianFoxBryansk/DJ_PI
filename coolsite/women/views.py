# для хранения представлений текущего приложения
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Страницу приложения видно")

def categories(request):
    return HttpResponse("<h1>Статьи по катигориям </h1>")

def moon(request):
    return HttpResponse("<h2> Это же МАРРИО- </h2>")
def moon1(request):
    return HttpResponse("Кот")
def moon2(request):
    return HttpResponse("<img src=https://dobrovserdce.ru/images/2022/11/02/kot%20Fedya_large.jpeg /img>")
