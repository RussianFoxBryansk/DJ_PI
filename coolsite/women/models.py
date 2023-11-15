#для хронения ORN моделей и придоставления данных из базы данных
from django.db import models

# Create your models here.
data_db = [{'id': 1, 'FIO': 'Снытко Руслан Николаевич', 'intresting': 'вязание, дизайн, верстка, вышивание крестиком',
            'diplom_red': True},
           {'id': 2, 'FIO': 'Король Богдан Александрович',
            'intresting': 'парашутный спорт, бокс , страйкбол,спортивный туризм', 'diplom_red': True},
           {'id': 3, 'FIO': 'Тузов Александр Максимович', 'intresting': 'курение, автомобили, спорт, компьютерные игры',
            'diplom_red': False},

           ]
# https://docs.djangoproject.com/en/4.2/ref/models/fields/
class  Students (models.Model):
    fio = models.CharField(max_length=50)
    interesting = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    dipolom_red = models.BooleanField(default=True)

class Gradebook (models.Model):
    lesson = models.CharField('Предмет',max_length=40)
    fio = models.CharField(max_length=100)
    date=models.DateField('Дата получения зачёта')


class Portfolio (models.Model):
    lesson = models.CharField('Предмет',max_length=40)
    text = models.TextField('Перечень всех достижений')
    date=models.DateTimeField('Дата создания')
