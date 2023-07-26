from django.db import models
from django.contrib.auth .models import User
# Create your models here.
#many to one 
class Product(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE) 
    user=models.ForeignKey(User,on_delete=models.PROTECT) # protect we can not delete user but cascade we can delete product and user
    Product_Name=models.CharField(max_length=50)
    Product_Price=models.IntegerField()
    Product_DT=models.DateField()
