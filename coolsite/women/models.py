#для хронения ORN моделей и придоставления данных из базы данных
from django.db import models

# Create your models here.
date_db =[{'id':1,'F10':'Снытко Руслан Николаевич','intresting':'вязание,дизайн,вёрстка,вышивание крестиком','diplom_red':True},
{'id':2,'F10':'Король Богдан Александрович','intresting':'вязание,дизайн,вёрстка,вышивание крестиком','diplom_red':True},
{'id':3,'F10':'Тузов Александр Максимович','intresting':'вязание,дизайн,вёрстка,вышивание крестиком','diplom_red':False},
]
class Students(models.Model):
    fio = models.CharField(max_length=50)
    intresting = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)