from django.http import HttpResponse
def fun(request):
    return HttpResponse("wellcome to views")

def fun2(request,arg):
    return HttpResponse(arg)

def fun3(request,arg):
    return HttpResponse(arg)
