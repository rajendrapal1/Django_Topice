from django.db import models
from tinymce.models import HTMLField 
# Create your models here.
class Model_class(models.Model):
    Title=models.CharField(max_length=50)
    Discription=HTMLField()
    field_name = models.FileField(upload_to='img/', max_length=254,default=None,)
