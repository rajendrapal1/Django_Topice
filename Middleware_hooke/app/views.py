from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse 

# Create your views here.
def My_views(request):
    return HttpResponse("welcome to my viewsfunction")

def excp_view(request):
    print("exceptin views")
    a=10/0
    return HttpResponse('exception ocoure')



def Temp_Response_fun(request):
   data={'name':'sonam'}
   return TemplateResponse(request,"Temp_Responce.html", data)
   