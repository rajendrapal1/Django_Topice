from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
def Myfun(request):
    print("my view function")
    return HttpResponse("my  meddleware function")

def Myclass_base(request):
    print("my class based views")
    return HttpResponse("my class based views")
