# для хранения представлений текущего приложения
from django.http import HttpResponse
from django.shortcuts import render
dir = {
        '1': ['Игнатьев А.А.',' 2001'],
        '2': ['Коновалов А.',' 2003'],
        '3': ['Тузов А. 2003'],
        '4': ['Ковалёв А. 2002'],
        '5': ['Король Б. 2002'],
        '6': ['Снытко Р. 2004'],
        '7': ['Лебедев Д. 2005'],
        '8': ['Мартыненко Д. 2005'],
        '9': ['Лелетко П. 2001'],
        '10': ['Селебин А. 2003'],
    }

# Create your views here.
def index(request):
    return HttpResponse("<a href=cod/>Страницу приложения видно 1</a><br><a href=cot/>Страницу приложения видно 2</a>")

def categories(request, cats_id):
    return HttpResponse(f"<h1>Статья под номером {cats_id}</h1>")
def categories_slug(request, cats):
    return HttpResponse(f"<h1>Статья под категории {cats}</h1>")

def students(request, students_id):
    if students_id>0 and students_id<=10:
        return HttpResponse(f"<h1>Студент {students_id}){dir[str(students_id)][0]} найден</h1>")
    else:
        return HttpResponse(f"<h1>Студента под номеромом {students_id} нет</h1>")

def students_slug(request, students):
    return HttpResponse(f"<h1>Статья про студента{students}</h1>")

def stud_slug(request, students):
    return HttpResponse(f"<h1>Статья про студента{students}</h1>")

def spisok(request,key):

    return HttpResponse(f"<h1> Список участников № {dir[key]} </h1>")

def moon(request):
    return HttpResponse("<h2> Это же МАРРИО- </h2>")
def moon1(request):
    return HttpResponse("Кот")
def moon2(request):
    return HttpResponse("<img src=https://dobrovserdce.ru/images/2022/11/02/kot%20Fedya_large.jpeg /img>")
date= {
        "2001": ['Игнатьев А.А. 28.06.2001','Лелетко П. 2001'],
        "2002": ['Ковалёв А. 2002','Король Б. 2002'],
        "2003": ['Студентов этого года нет'],
        "2004": ['Тузов А. 2004','Коновалов А. 2004','Снытко Р. 2004','Лебедев Д. 2004','Селебин А. 2004'],
        "2005": ['Мартыненко Д.Д 2005'],

    }
def date(request,datee):
    dir = {
        "2001": ['Игнатьев А.А. 28.06.2001','Лелетко П. 2001'],
        "2002": ['Ковалёв А. 2002','Король Б. 2002'],
        "2003": ['Студентов этого года нет'],
        "2004": ['Тузов А. 2004','Коновалов А. 2004','Снытко Р. 2004','Лебедев Д. 2004','Селебин А. 2004'],
        "2005": ['Мартыненко Д.Д 2005'],

    }
    if datee > 2001 and datee < 2005:
        return HttpResponse(f"<h1> Студенты {dir[str(datee)]} найдены </h1>")
    else:
        return HttpResponse(f"<h1>Студента с таким годом {datee} нет</h1>")