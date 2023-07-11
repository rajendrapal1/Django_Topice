from django.http import HttpResponse
from django.shortcuts import render

def fun(request):
    return render(request,"render.html")

def fun1(request):
    return HttpResponse("wellcome to python")

def fun2(request,arg): # get dynamic data from the urls
    return HttpResponse(arg)