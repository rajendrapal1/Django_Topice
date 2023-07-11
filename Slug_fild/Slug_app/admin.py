from django.contrib import admin
from Slug_app.models import Model_class
from django.contrib.admin.sites import site
# Register your models here.
class Adimi_class(admin.ModelAdmin):
    list_display=('Fild_title','Fild_Discription','slug_data')
admin.site.register(Model_class,Adimi_class)