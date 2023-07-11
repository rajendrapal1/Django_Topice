from django.contrib import admin
from News_App .models import Model_class
from django.contrib.admin.sites import site


# Register your models here.
class Admin_class(admin.ModelAdmin):
    list_display=['News','Discription1','Discription2',]
admin.site.register(Model_class,Admin_class)
# admin.site.register(Admin_class)