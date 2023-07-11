from django.shortcuts import render  # send data views to templates
from django.http import HttpResponse # send data views to server

#student detale
def student(request):
    dic= { 

          'list':    ['raj','2','surat'],

          'stu_roll':[10,20,30,40,50],


          'stu_details':[
              {'name':'raj','roll':123456789,'marks':60},
              {'name':'aman','roll':1234234567,'marks':70}
          ]

              
    }    
    return render(request,'temp.html',dic)

#dyanmic Urls => send data to server

def title(request,name):
    return HttpResponse(name)    