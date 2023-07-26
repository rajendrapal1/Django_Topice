from django.db import models

# Create your models here.
class GenericView_List(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    city=models.CharField(max_length=30)
