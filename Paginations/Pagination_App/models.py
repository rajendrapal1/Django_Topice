from django.db import models

from tinymce.models import HTMLField 
# Create your models here.

class Model_class(models.Model):
    Page=models.CharField(max_length=50)
    Page_Details=HTMLField()
    
