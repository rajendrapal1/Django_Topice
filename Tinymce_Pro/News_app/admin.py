from django.contrib import admin
from News_app.models import Model_class
from django.contrib.admin.sites import site


# Register your models here.
class Admin_class(admin.ModelAdmin):
    list_display=('New_title','New_discription')
admin.site.register(Model_class,Admin_class)    

 