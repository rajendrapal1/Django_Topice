from django.http import HttpResponse  # HttpResponce use send data view to servers  
from django.shortcuts import render   # render views to template

def form_get_data(request):
    data={
        'title':'homepage',
        'name':'wellcome to python'
    }
    return render(request,"tem.html",data)

def dynamic_data(request,arg):
    return HttpResponse(arg) 

def fun(request):
    return HttpResponse("wellcome to python")