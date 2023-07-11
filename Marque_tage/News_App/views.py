from django.shortcuts import render
from News_App.models import Model_class

# Create your views here.
def News(request):
    get_data=Model_class.objects.all()
    dic={'dt':get_data}
    return render(request,'temp.html',dic)
