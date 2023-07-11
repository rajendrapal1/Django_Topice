from django.contrib import admin
from App_Filter .models import Model_class
from django.contrib.admin.sites import site

# Register your models here.
class Model_admin(admin.ModelAdmin):
    list_display=('name','email','address')

admin.site.register(Model_class,Model_admin)    
