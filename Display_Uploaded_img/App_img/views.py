from django.shortcuts import render
from App_img .models import Model_class
# Create your views here.

def Display_deta(requst):
    data=Model_class.objects.all()

    return render(requst,'home_page.html',{'dt':data})
