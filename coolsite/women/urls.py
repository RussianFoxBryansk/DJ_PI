from django.urls import path, register_converter

from women.classconverter import FourDigitYearConverter
from women.views import *

register_converter(FourDigitYearConverter,"yyyy")

urlpatterns = [

    path('',index, name = 'home'),
    path('cat/',categories, name ='cat'),
    path('mario/',moon, name ='mario'),
    path('cot/',moon1,name ='cot'),
    path('cod/',moon2,name ='cod'),
    path('test/',index1,name ='test'),
    path('cats/<int:cats_id>/', categories,name ='cats1'),
    path('cats/<slug:cats>/', categories_slug,name ='cats2'),
    path('students/<int:students_id>/', students,name ='students1'),
    path('students/<slug:students>/', students_slug,name ='students2'),
    path('studo/<slug:students>/', stud_slug,name ='mario'),
    path("spisok/<int:key> ",spisok,name ='studo'),
    path('date/<int:datee>/',date,name ='date'),
    path('articles/<yyyy:year>/',year_archive,name ='articles'),
    path('DATA/', save_data, name='GET'),
    path('GET_13/',post_detail),
]

