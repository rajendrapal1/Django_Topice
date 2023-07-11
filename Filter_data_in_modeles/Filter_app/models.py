from django.db import models
from tinymce.widgets import TinyMCE 
from tinymce.models import HTMLField
from autoslug import AutoSlugField
# Create your models here.
class Model_Class(models.Model):
    subject=models.CharField(max_length=50)
    Discrption=HTMLField()
    slug= AutoSlugField(populate_from='subject',unique=True ,null=True,default=None)


