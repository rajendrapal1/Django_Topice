from django.db import models
from tinymce.models import HTMLField
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    Title=models.CharField(max_length=50)
    Discription=HTMLField()
    # Img=models.ImageField(upload_to='img', height_field=230, width_field=230, max_length=200,)
    Img=models.FileField(upload_to='media/',max_length=220,null=True,default=None)
    release_date=models.DateField(default=datetime.now().date())
    
    
