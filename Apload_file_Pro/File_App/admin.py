from django.contrib import admin

from django.contrib.admin.sites import site
from File_App.models import Model_class
# Register your models here.
class Admin_class(admin.ModelAdmin):
    list_display=('Title','Discription','New_img')
admin.site.register(Model_class,Admin_class)    