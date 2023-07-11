from django.shortcuts import render
from App_data . models import Model_class 
# Create your views here.
def Save_form(request):
    dt=''
    
    if request.method=='POST':
        N_name=request.POST.get('name')
        E_name=request.POST.get('email')
        P_name=request.POST.get('password')
        Pn_name=request.POST.get('num')
        ws_name=request.POST.get('webside')
                                                                                  
                                                                                  
        data=Model_class(
            name=N_name,
            email=E_name,
            password=P_name,
            number=Pn_name,
            weside=ws_name,
            
            
        )
        data.save()
        dt="data inserted successfull"


    else:
        pass    
    return render(request,'homepage.html',{'n':dt})
# ss Model_class(models.Model):
#     name=models.CharField(max_length=50)
#     email=models.EmailField(max_length=50)
#     password=models.CharField(max_length=50)
#     number=models.IntegerField()
#     weside=models.CharField(max_length=50)
