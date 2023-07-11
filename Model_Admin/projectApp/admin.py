from django.contrib import admin
from projectApp .models import model_fild
from django.contrib.admin.sites import site
# Register your models here.
class Admin_fun (admin.ModelAdmin):
    list_display=('name','email')
    
admin.site.register(model_fild,Admin_fun)    
