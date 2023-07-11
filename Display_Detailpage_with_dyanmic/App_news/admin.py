from django.contrib import admin

# Register your models here.
from App_news.models import Model_class
from django.contrib.admin.sites import site


# Register your models here.
class Admin_class(admin.ModelAdmin):
    list_display=('News_title','News_discription', 'slug_data')
admin.site.register(Model_class,Admin_class)    

 