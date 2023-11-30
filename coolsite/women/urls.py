from django.urls import path, register_converter

from women import views
from women.classconverter import FourDigitYearConverter
from women.views import *

register_converter(FourDigitYearConverter,"yyyy")

urlpatterns = [

    path('',index, name = 'home'),
    path('cat/',categories, name ='cat'),
    path('about/',about,name ='about'),
    path('categor/', categ, name='cats'),
    path('mario/',moon, name ='mario'),
    path('cot/',moon1,name ='cot'),
    path('cod/',moon2,name ='cod'),
    path('test/',index1,name ='test'),
    path('cats/<int:cats_id>/', categories,name ='cats1'),
    path('cats/<slug:cats>/', categories_slug,name ='cats2'),
    path('students/<int:students_id>/', students1,name ='student2'),

    path('students1/', students, name='students1'),
    path('students1/<slug:students_slug>/', student, name='student'),

    path('students/<slug:students>/', students_slug,name ='students2'),
    path('studo/<slug:students>/', stud_slug,name ='mario'),
    path("spisok/<int:id> ",spisok,name ='studo'),
    path('date/<int:datee>/',date,name ='date'),
    path('articles/<yyyy:year>/',year_archive,name ='articles'),
    path('DATA/', save_data, name='GET'),
    path('GET_13/',post_detail,name='get-13'),
    path('spisok_st/<int:spisok_id>/', views.show_spisok, name='spisok_st'),
    path('cub/',cub,name='cub'),
    path('book/',Book_name)

]

