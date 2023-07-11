from django .shortcuts import render
from App_Filter .models import Model_class



def Filter_fun(request):
   Model_getdata=Model_class.objects.all().order_by('name')
   data={'dt':Model_getdata}
   return render(request,'temp.html', data)