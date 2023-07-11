from django.contrib import admin
from Filter_app.models import Model_Class
from django.contrib.admin.sites import site

# Register your models here.
class Admin_Class(admin.ModelAdmin):
    list_display=('subject','Discrption')
admin.site.register(Model_Class,Admin_Class),    

