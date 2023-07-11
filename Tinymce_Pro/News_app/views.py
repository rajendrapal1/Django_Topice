from django.shortcuts import render
from News_app.models import Model_class

# Create your views here.
def Display_data(request):
    
    get_data=Model_class.objects.all()
    print(get_data)
    data={'dt':get_data}


    return render(request,'temp.html',data)
