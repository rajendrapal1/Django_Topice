from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def setsession(request):
    request.session['name']='Teamopine'
    data=render (request,'set_session.html')


def Get_session(request):
    obj=request.session.get('name')
    return render(request,'get_session.html',{'dt':obj})

def Delete_session(request):
    request.session.flush()
    request.session.clear_expierd()

        