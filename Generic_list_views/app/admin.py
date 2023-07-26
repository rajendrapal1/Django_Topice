from django.contrib import admin
from app .models import GenericView_List
# Register your models here.
@admin.register(GenericView_List)
class GenericListAdmin(admin.ModelAdmin):
    list_display=('name','email','city')
    