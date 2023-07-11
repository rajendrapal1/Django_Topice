from django.contrib import admin
from Bolock_App.models import Blog
from django.contrib.admin.sites import site
# Register your models here.
#@admin.register(Blog)
class Admin_Blog(admin.ModelAdmin):
    list_display=('id','Title','Discription','Img','release_date')
admin.site.register(Blog,Admin_Blog)    
    
