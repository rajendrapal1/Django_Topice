from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
# Create your views here.

def setsession(request):
    request.session['name']='Team opine'
    response= render(request,'setdata.html')
    
    response.set_cookie('name',  max_age=3560)
    return response


def getsession(request):
    if 'name' in request.session:
        obj=request.session['name']
        request.session.modified=True  # modified method if i do refress then time is incries 
    
        return render(request,'get_session.html',{'dt':obj})
    else:
        return HttpResponse("session id expire")
    

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return HttpResponse (request,'delete_session.html')
    