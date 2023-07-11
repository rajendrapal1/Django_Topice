from django.shortcuts import render
from app_models.forms import Studen_Registations
# Create your views here.
def Model_forms(request):
    data=Studen_Registations()








    # if request.method=="POST":
    #     Nname=Model_forms.object.GET.get('name'),
    #     Nname=Model_forms.object.GET.get('email'),
    #     Nname=Model_forms.object.GET.get('password'),
    
    
    return render(request,'form.html',{'dt':data})
