from django.contrib import admin
from .models import *

# Register your models here.
class GonggoAdmin(admin.ModelAdmin):
    list_display = ['id','title','main_category','company_names']

admin.site.register(Gonggo, GonggoAdmin)