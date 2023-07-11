from django.db import models

#Create your models here.
class Model_class(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    number=models.IntegerField()
    weside=models.CharField(max_length=50)

