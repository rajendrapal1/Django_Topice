from django.contrib import admin
from app .models import ModelPage

# Register your models here.

@admin.register(ModelPage)
class AdminClass(admin.ModelAdmin):
    list_display=['user','PageName','PageNumb','Page_Duretions'] 