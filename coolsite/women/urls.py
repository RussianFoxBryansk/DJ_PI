from django.urls import path, register_converter

from women.classconverter import FourDigitYearConverter
from women.views import *

register_converter(FourDigitYearConverter,"yyyy")

urlpatterns = [

    path('',index, name = 'home'),
    path('cat/',categories, name ='cat'),
    path('mario/',moon, name ='mario'),
    path('cot/',moon1,),
    path('cod/',moon2),
    path('test/',index1),
    path('cats/<int:cats_id>/', categories),
    path('cats/<slug:cats>/', categories_slug),
    path('students/<int:students_id>/', students),
    path('students/<slug:students>/', students_slug),
    path('studo/<slug:students>/', stud_slug),
    path("spisok/<int:key> ",spisok),
    path('date/<int:datee>/',date),
    path('articles/<yyyy:year>/',year_archive),
]

