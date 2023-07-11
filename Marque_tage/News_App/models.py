from django.db import models

from tinymce.models import HTMLField
# Create your models here.

class Model_class(models.Model):
    News=models.CharField(max_length=50)
    Discription1=models.CharField(max_length=50)
    Discription2=HTMLField()