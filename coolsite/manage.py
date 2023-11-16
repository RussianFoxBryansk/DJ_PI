#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coolsite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

'''DB
    python manage.py makemigtation создание миграции
    
    python manage.py sqlmigtate women 0001 просмотр миграции на sql
    
    python manage.py migrate выполнение миграции
    
    python manage.py shell_plus --print-sql работа с бд
    In [3]: w1= Students(fio='Снытко Руслан Николаевич',interesting ='вязание, дизайн, верстка, вышивание крестиком',dipolom_red = True)

    In [4]: w1.save()
    Students.objects.create(fio='Король Богдан Александрович',interesting ='парашутный спорт, бокс , страйкбол,спортивный туризм',dipolom_red = True )
    


'''
#python manage.py collectstatic сщбирает статические файлы перед выгрузкой на сервер
# python manage.py runserver --insecure
if __name__ == '__main__':
    main()
