from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ModelPage(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    PageName=models.CharField(max_length=50)
    PageNumb=models.IntegerField()
    Page_Duretions=models.DateField()
