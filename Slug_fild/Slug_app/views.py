from django.shortcuts import render
from Slug_app.models import Model_class

#Create your views here.

def Home_page(request):
    
    slugdata=Model_class.objects.all()
    data={'dt':slugdata}
    return render(request,'homepage.html',data)


def About_page(request,slugdata):

   
     data=Model_class.objects.filter(slug_data=slugdata)
     print(data)
     dic={'dt':data}

     return render(request,'about.html',dic)
    


# from django.shortcuts import render
# from App_news .models import Model_class

# # Create your views here.
# def novebar(request):
#      data=Model_class.objects.all()
#      obj={'dt':data}

#      return render(request,'temp.html',obj)



# def home_page(request,slugdata):  # slug field use 
#      print(slugdata)
     
#      data=Model_class.objects.filter(slug_data=slugdata)
#      print(data)
#      dic={'dt':data}

#      return render(request,'homepage.html',dic)