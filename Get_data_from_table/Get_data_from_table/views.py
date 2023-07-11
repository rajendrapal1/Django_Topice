from django .shortcuts import render
from app_1 .models import model_form

def Temp_fun(request):
    data=model_form.objects.all().order_by('-name') [:1] # we can set lime of data  
    data=model_form.objects.all().order_by('name')  #get data in accending order and decending order
    data=model_form.objects.all()
    data1={'dt':data}

    return render(request,'temp.html',data1)