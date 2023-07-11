from django.contrib import admin
from App_data.models import Model_class
from django.contrib.admin.sites import site
# Register your models here.
class Admin_class(admin.ModelAdmin):
    list_display=('name','email','password','number','weside')
admin.site.register(Model_class , Admin_class)    
