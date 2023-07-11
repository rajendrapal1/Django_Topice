from django.shortcuts import render
from Filter_app .models import Model_Class
# Create your views here.
def Home_page(request):
    all_data=Model_Class.objects.all()
    var_dic={'dt':all_data}

    return render(request,'homepage.html',var_dic)


#searching data from the models using filter 
def Show_data(request):

    if request.method=='GET':
       data=request.GET.get('searchdata')
       print(data)
       if data:
        response=Model_Class.objects.filter(subject__icontains=data)
       else:
        response="no data fouuntd"

       dic={
          
           'dt':response
        }
    
       return render(request,'show_data.html',dic)