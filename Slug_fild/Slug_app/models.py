from django.db import models
from tinymce.models import HTMLField 
from autoslug import AutoSlugField

# Create your models here.
class Model_class(models.Model):
    
    Fild_title=models.CharField(max_length=50)
    Fild_Discription=HTMLField()
    slug_data=AutoSlugField(populate_from='Fild_title',unique=True,null=True,default=None)






