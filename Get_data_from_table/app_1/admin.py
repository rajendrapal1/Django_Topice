from django.contrib import admin
from app_1.models import model_form
from django.contrib.admin.sites import site
# Register your models here.
class adminclass(admin.ModelAdmin):
    list_display=('name','email','address')
admin.site.register(model_form,adminclass)    

