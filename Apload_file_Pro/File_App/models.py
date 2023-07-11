from django.db import models
from tinymce.models import HTMLField 

# Create your models here.
class Model_class(models.Model):
    Title=models.CharField(max_length=50)
   
    Discription=HTMLField()

    New_img=models.FileField(upload_to='media/',max_length=220,null=True,default=None)
