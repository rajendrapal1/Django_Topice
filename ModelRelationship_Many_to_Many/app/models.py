from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user=models.ManyToManyField(User)
    Product_Name=models.CharField(max_length=40)
    Product_Price=models.IntegerField()

    def Getdata(self):
        return ",".join([str(data) for data in self.user.all()])