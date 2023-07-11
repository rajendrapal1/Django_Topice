from django.http import HttpResponse # send data views to servers
from django.shortcuts import render # render views to template file data

def Data_to_server(request):
    return HttpResponse("Wellcome to data")

def Data_send_to_temp(request):
    data={
          'title':"homepage",
          'name':'python',

          'list':['iicss','collage','surat'],
        
        
          'student':[
            
                  {'name':'padip','roll':1},
                  {'name':'raj','roll':2},
        
                 ]  
        }
     
    # for i in data.items():
    #      print(i)    

    return render(request, 'temp.html',data)
