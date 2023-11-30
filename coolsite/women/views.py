# для хранения представлений текущего приложения
from contextvars import Context

from django.core.exceptions import SuspiciousOperation, PermissionDenied
from django.http import HttpResponse, HttpResponseNotFound, Http404

from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify, upper
from django.template.loader import render_to_string

from django.views.decorators.csrf import requires_csrf_token
from .models import Book, Students


def Book_name(request):
    book_inf = Book.objects.all()
    print(book_inf)
    return render(request, 'women/book.html', {'kkk':book_inf})

def ServerError(request):
    return HttpResponseNotFound( '<h1>ошибка сервера<h1>')

def AccessBan(request, exception):
    print(exception)
    return HttpResponseNotFound('<h1>нет доступа<h1>')

def SearchError(request, exception):
    print(exception)
    return HttpResponseNotFound('Ошибка 400')

date_db =[{'id':1,'F10':'Снытко Руслан Николаевич','intresting':'вязание,дизайн,вёрстка,вышивание крестиком','diplom_red':True},
{'id':2,'F10':'Король Богдан Александрович','intresting':'вязание,дизайн,вёрстка,вышивание крестиком','diplom_red':True},
{'id':3,'F10':'Тузов Александр Максимович','intresting':'вязание,дизайн,вёрстка,вышивание крестиком','diplom_red':False},
]




def students(request):
    posts = Students.objects.all()
    data={'title': 'Список студентов',
            'menu': menu,
            'posts': posts,
          }
    return render(request, 'women/students.html', data)
def student(request, student_slug):
    post = get_object_or_404(Students, slug=student_slug)
    data={'title': 'Профиль студента',
            'menu':menu,
            'post':post,
          }
    return render(request, 'women/student.html', data)







def show_spisok(request, spisok_id):
    return HttpResponse(f"Отображение списка студента = {spisok_id}")

spisok_db = [
    {'id' : 1, 'title' : 'Игнатьев А.А.', 'content': '28.06.2001','is_published': True},
    {'id': 2, 'title': 'Коновалов А.', 'content': '2004','is_published': True},
    {'id': 3, 'title': 'Тузов А.', 'content': '2004','is_published': True},
    {'id': 4, 'title': 'Ковалёв А.', 'content': '2002','is_published': True},
    {'id': 5, 'title': 'Король Б.', 'content': '2002','is_published': True},
    {'id': 6, 'title': 'Снытко Р.', 'content': '2004','is_published': True},
    {'id': 7, 'title': 'Лебедев Д.', 'content': '2004','is_published': False},
    {'id': 8, 'title': 'Мартыненко Д.', 'content': '2005','is_published': True},
    {'id': 9, 'title': 'Лелетко П.', 'content': '2001','is_published': True},
    {'id': 10, 'title': 'Селебин А.', 'content': '2004','is_published': True},
]

dir = {
        '1': ['Игнатьев А.А. 2001 <img src=https://sun9-27.userapi.com/impg/JNzAbn8urKhcjob4gd2CQcU_NTJfNg_A7T9Ejw/_xV4TRKU0EA.jpg?size=811x1080&quality=95&sign=a268f9baeda96f75c27de216b69a4953&type=album /img>'],
        '2': ['Коновалов А. 2003 <img src=https://sun9-79.userapi.com/impg/k38olU6WffjL8depG564PuzZHIKllRHMWNC-aA/UIqWYqpQePA.jpg?size=810x1080&quality=95&sign=34e14f0a67801a8cb170443a8ad51aaf&type=album /img>'],
        '3': ['Тузов А. 2003 <img src=https://sun136-2.userapi.com/impg/zkn9lD3tysQVUso18BhjtSE-sIRzvOM1CUKcWA/z_QJIqFIAfU.jpg?size=810x1080&quality=95&sign=8aa9ceb190884005afa65629f8c915a0&type=album /img>'],
        '4': ['Ковалёв А. 2002 <img src=https://sun9-37.userapi.com/impg/bO1t4LI8qu-8HwFOnvBQZK4o33a1yzsKBcXTjA/1hv0Ejufq-4.jpg?size=810x1080&quality=95&sign=3f6b0582a5454c309cf49b7df746b045&type=album /img>'],
        '5': ['Король Б. 2002 <img src=https://dobrovserdce.ru/images/2022/11/02/kot%20Fedya_large.jpeg /img>'],
        '6': ['Снытко Р. 2004 <img src=https://sun9-68.userapi.com/impf/c856032/v856032815/5f2bd/Uj6Yd91AOxk.jpg?size=442x798&quality=96&sign=e59e51d05a69f52665f1536a65255c0f&type=album /img>'],
        '7': ['Лебедев Д. 2005 <img src=https://dobrovserdce.ru/images/2022/11/02/kot%20Fedya_large.jpeg /img>'],
        '8': ['Мартыненко Д. 2005 <img src=https://sun9-20.userapi.com/impg/nu1uHk67M2uTAcNXTb6RobDvwCyWlyEtfY5Sfg/gleirB67Rn8.jpg?size=720x1080&quality=95&sign=b3e6f009fd83ad706c4d231ad8e875c1&type=album /img>'],
        '9': ['Лелетко П. 2001 <img src=https://sun9-13.userapi.com/impg/MGOyyiRmCLp2YHFdhV3lNp0mm7YbPoPFzxUq2w/MBWNi0q-ufc.jpg?size=788x1054&quality=96&sign=80a1e163625a968363481eb211dbcc06&type=album /img>'],
        '10': ['Селебин А. 2003 <img src=https://sun9-5.userapi.com/impg/cjKqAfTRhGPtfkUHnv2DdoP-qt86Q24cu5ivSg/m5OrXce2Xo0.jpg?size=592x663&quality=95&sign=e9843300af1cc1fe9eea6dbd393df15f&type=album /img>'],
    }

def index1(request):
    print(request.GET)
    return HttpResponse(f"страница приложения women{dict(request.GET)}")


menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Домашняя', 'url_name': 'home'},
        {'title': 'Категории', 'url_name': 'cats'},
        {'title': 'Красивый css', 'url_name': 'cub'},
        {'title': 'кот', 'url_name': 'cat'},
        {'title': 'маррио', 'url_name': 'mario'},
        {'title': 'кот-но не кот', 'url_name': 'cot'},
        {'title': 'код', 'url_name': 'cod'},
        {'title': 'Тест', 'url_name': 'test'},
        {'title': 'get-13', 'url_name': 'get-13'},
        {'title': 'Студенты', 'url_name': 'students1'},
        ]

def about(request):
    return render(request, 'women/about.html', context={'menu': menu, 'title': 'О программе'})


def cub(request):
    return render(request, 'women/3D_kub.html', context={'menu': menu, 'title': 'Красивый css'})

class MyClass:
    def __init__(self, a,b):
        self.a = a
        self.b = b
def index(request):
    #t =render_to_string('women/index.html')
    #return HttpResponse(t)
    data={'title': 'Главная',
            'menu':menu,
            'float':23.123,
            'value': 1,
            'url': slugify ("OCHEN KRUTOY KURSACH"),
            'dict': {'маррио':'28.09.1999'},
            'set': "a,b,c",
            'int': 2023,
          'tup': [1, 2.0, "hello"],
          'bool': True,
          'list': [1, 2, 'abc', True],
          'set1': {1, 1, 2, 3, 2, 5},
          'dict1': {'key_1': 'value_1', 'key_2': 'value_2'},
         'obj': MyClass(10, 20),
          'posts':date_db,
          'spisok': spisok_db,
          }
    data_txt={}
    return render(request,'women/index.html',context=data)
# Create your views here.
def post_detail(request):
    get_params = dict(request.GET)
    if get_params:
        print(request.GET)
        for i,k in  get_params.items():
            print(i,k)
        response_string = ''
        for k, v in get_params.items():
            response_string += f'{k} = {v} | '
        return HttpResponse(response_string)
    else:
        return HttpResponse("GET is empty")

def categ(request):
    return HttpResponse("<h1> Страница с номером категорий </h1>")

def categories(request, cats_id):
    return HttpResponse(f"<h1>Статья под номером {cats_id}</h1>")

def categories_slug(request, cats):
    return HttpResponse(f"<h1>Статья под категории {cats}</h1>")

def students1(request, students_id):
    if students_id>0 and students_id<=10:
        return HttpResponse(f"<h1>Студент {students_id}){dir[str(students_id)][0]} найден</h1>")
    if students_id ==-1:
        return redirect('test', permanent=True)
    else:
        raise Http404()

def students_slug(request, students):
    return HttpResponse(f"<h1>Статья про студента{students}</h1>    ")

def stud_slug(request, students):
    return HttpResponse(f"<h1>Статья про студента{students}</h1>")

def spisok(request,id):

    return HttpResponse(f"<h1> Список участников № {dir[id]} </h1>")

def moon(request):
    return HttpResponse("<h2> Это же МАРРИО- </h2>")
def moon1(request):
    return render(request,'cookie/index.html')
def moon2(request):
    return HttpResponse("<img src=https://dobrovserdce.ru/images/2022/11/02/kot%20Fedya_large.jpeg /img>")

def date(request,datee):
    dir = {
        "2001": ['Игнатьев А.А. 28.06.2001','Лелетко П. 2001'],
        "2002": ['Ковалёв А. 2002','Король Б. 2002'],
        "2003": ['Студентов этого года нет'],
        "2004": ['Тузов А. 2004','Коновалов А. 2004','Снытко Р. 2004','Лебедев Д. 2004','Селебин А. 2004'],
        "2005": ['Мартыненко Д.Д 2005'],

    }
    if datee ==2009:
        return redirect('mario', permanent=True)
    if datee > 2001 and datee < 2005:
        return HttpResponse(f"<h1> Студенты {dir[str(datee)]} найдены </h1>")
    else:
        return HttpResponse(f"<h1>Студента с таким годом {datee} нет</h1>")

def pageNotFound(request,exception):
    print(exception)
    return HttpResponseNotFound(f"<h1>Страница не найдена{exception}</h1>")

def year_archive(request,year):
    if (int(year))== 1000:
        raise SuspiciousOperation
    if (int(year))==1100:
        raise PermissionDenied
    if (int(year))==1110:
        raise Context
    if (int(year))> 2023:
        raise Http404()
    if (int(year))==2000:
        return redirect('home',permanent=True)
    return HttpResponse(f"<h1>год изменения {year}</h1>")

def save_data(request):
    if request.method == 'GET':
        data = request.GET.get('GET', '')
        with open('GET.txt', 'a') as file:
            file.write(data + '\n')
        return HttpResponse('Данные успешно записаны в файл')
    else:
        return HttpResponse('Метод запроса должен быть GET')



def split_line(line, sep):
    if not line:
        return ['']
    list1=[]
    sim=""
    cav = False
    for i in line:
        if '"'  in i:
            cav = not cav
        if sep in i and cav == False :
            list1.append(sim.replace('"',''))
            sim = ""
        else:
            sim += i
    list1.append(sim.replace('"',''))
    return list1



def read_split_line_tests():
    example_1_line = 'Александр Александрович Александров,,2005,11'
    example_1_sep = ','
    example_1_res = ['Александр Александрович Александров', '', '2005', '11']

    print(split_line(example_1_line, example_1_sep), example_1_res)

    example_2_line = 'Евгений Сергеевич Дёмин;;'
    example_2_sep = ';'
    example_2_res = ['Евгений Сергеевич Дёмин', '', '']

    print(split_line(example_2_line, example_2_sep), example_2_res)

    example_3_line = 'Анна Павловна Иванова,"[запись 1, запись 2, запись 3]", ,2'
    example_3_sep = ','
    example_3_res = ['Анна Павловна Иванова', '[запись 1, запись 2, запись 3]', ' ', '2']

    print(split_line(example_3_line, example_3_sep), example_3_res)

    print('Все тесты прошли успешно!')

