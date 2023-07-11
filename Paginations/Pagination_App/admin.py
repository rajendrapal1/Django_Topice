from django.contrib import admin
from Pagination_App .models import Model_class
from django.contrib.admin.sites import site
#@admin.register(Model_class)
#or
# Register your models here.
class Admin_class(admin.ModelAdmin):
    list_display=('id','Page','Page_Details')
admin.site.register(Model_class,Admin_class)    

