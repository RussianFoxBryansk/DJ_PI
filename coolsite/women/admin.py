# для настройки админ-панели сайта
from django.contrib import admin
from  .models import Gradebook
from  .models import Students
from  .models import Portfolio
from  .models import Book

admin.site.register(Gradebook)
admin.site.register(Students)
admin.site.register(Portfolio)
admin.site.register(Book)
# Register your models here.
