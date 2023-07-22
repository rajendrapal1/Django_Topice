from django.shortcuts import render
from Apps .forms import Signup_Form
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
# Create your views here.



def signupforms(request):
    if request.method=='POST':
        FM=Signup_Form(request.POST)
        if FM.is_valid():
            FM.save()
    else:
        FM=Signup_Form()

    return render(request,'signup.html',{'dt':FM})

 

def login_forms(request):
    if request.method=="POST":
        fm=AuthenticationForm(request.POST,data=request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            check_auth=authenticate(username=name,password=password)  
            if check_auth is not None:
                 login(request,check_auth)
                 return HttpResponseRedirect('/dashboard/')
            
    else:
             fm=AuthenticationForm()
    return render(request,'login_forms.html',{'dt':fm})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')
    


def Dasboard(request):
     if request.user.is_authenticated:
       
       return render(request,'dasboard.html',{'name':request.user.username})
       
     
     
     
     return HttpResponseRedirect('logout/')







# def login_page(request):
#    if request.method=="POST":
#       data=AuthenticationForm(request.POST,data=request.POST)
#       if data.is_valid():
#          uname=data.cleaned_data['username']
#          upass=data.cleaned_data['password']   
#          dt=authenticate(username=uname,password=upass)
#          if dt is not None:
#             login(request,dt)
#             messages.success(request, "Login successful." ) # messages send at prfile page
#             return HttpResponseRedirect('/profile/')     
#    else:
#       data=AuthenticationForm()
#    return render(request,'login.html',{'DT':data})


