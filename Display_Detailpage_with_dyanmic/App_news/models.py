
from django.db import models
from tinymce.models import HTMLField   # if we  want to add,itailic,bold,underline model in fild  data and
from autoslug import AutoSlugField
# Create your models here.

class Model_class(models.Model):
    News_title=models.CharField(max_length=50)
    News_discription=HTMLField()

    slug_data=AutoSlugField(populate_from='News_title',unique=True,null=True,default=None)
  



# from autoslug import AutoSlugField
# # Create your models here.
# class Model_Class(models.Model):
#     subject=models.CharField(max_length=50)
#     Discrption=HTMLField()
#    

