"""
URL configuration for coolsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


# настройка адрисной строки
from women.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('women/',include('women.urls')),
    path('cats/<int:cats_id>/', categories),
    path('cats/<slug:cats>/', categories_slug),
    path('students/<int:students_id>/', students),
    path('students/<slug:students>/', students_slug),
    path('studo/<slug:students>/', stud_slug),
    path("spisok/<int:key> ",spisok),
    path('date/<int:datee>/',date),
]
