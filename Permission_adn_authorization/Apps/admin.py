from django.contrib import admin
from Apps.models import Blog

@admin.register(Blog)
# Register your models here.
class Adin_class(admin.ModelAdmin):
    list_display=('title','dsce')