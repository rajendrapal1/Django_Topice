from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def My_views_fun(request):
#     print("my views fun")
#     return HttpResponse("welcome to my views function")


# class baseviews

def Middleware_views(request):
    print("view function excute")
    return HttpResponse("wellcome to views function")