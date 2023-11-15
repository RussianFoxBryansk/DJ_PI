# для настройки админ-панели сайта
from django.contrib import admin
from  .models import Gradebook
from  .models import Students
from  .models import Portfolio

admin.site.register(Gradebook)
admin.site.register(Students)
admin.site.register(Portfolio)
# Register your models here.
