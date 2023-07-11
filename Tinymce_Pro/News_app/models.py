from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Model_class(models.Model):
    New_title=models.CharField(max_length=50)
    New_discription=HTMLField()

