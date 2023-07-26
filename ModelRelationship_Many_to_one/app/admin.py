from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)

class Product_Admin(admin.ModelAdmin):
    list_display=['user','Product_Name','Product_Price','Product_DT']

