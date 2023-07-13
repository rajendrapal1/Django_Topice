

# Create your views here.
from django.shortcuts import render 
from app .forms import User_forms,edit_user_form
# from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponseRedirect
from django.contrib import messages #import messages
# Create your views here.

#Create signup page

def Signup_fun(request):
    if request.method=='POST':
      fm=User_forms(request.POST)
      
      if fm.is_valid():
       fm.save()
       messages.success(request,'Signup successful')
    else:  
       fm=User_forms()      
    return render(request,'signup_page.html',{'dt':fm})


#login page
def login_page(request):
   if request.method=="POST":
      data=AuthenticationForm(request.POST,data=request.POST)
      if data.is_valid():
         uname=data.cleaned_data['username']
         upass=data.cleaned_data['password']   
         dt=authenticate(username=uname,password=upass)
         if dt is not None:
            login(request,dt)
            messages.success(request, "Login successful." ) # messages send at prfile page
            return HttpResponseRedirect('/profile/')     
   else:
      data=AuthenticationForm()
   return render(request,'login_page.html',{'DT':data})

#profile page update 
def profile_page(request):
    if request.user.is_authenticated:
      if request.method=="POST":
         data=edit_user_form(request.POST,instance=request.user)
         if data.is_valid():
            print(data)
            data.save()
         # data=edit_user_form(instance=request.user)
         messages.success(request,'profile updat successful')

      else:
              data=edit_user_form()
      return render (request,'profile.html',{'dt':data})
    else:
           return HttpResponseRedirect('/login/')
      

#change password
def change_pass(request):
   if request.user.is_authenticated: # pree define method
      if request.method=="POST":
         data=PasswordChangeForm(user=request.user,data=request.POST)
         if data.is_valid():
            data.save()
            update_session_auth_hash(request, data.user)

            return HttpResponseRedirect('/login/')
      else:
         data=PasswordChangeForm(user=request.user)
   
      return render(request,'change_pass.html',{'dt':data})
   else:

    return HttpResponseRedirect('/login/')
   


# chench password only two field
def change_pass2(request):
   if request.method=='POST':
      data=SetPasswordForm(user=request.user,data=request.POST)
      if data.is_valid():
         data.save()
         update_session_auth_hash(request,data.user)
         return HttpResponseRedirect('/login/')
   else:
      data=data=SetPasswordForm(user=request.user) 
   return render(request,'chenge_pass2.html',{'dt':data})   


#logout 
def logout(request):
   logout(request)
   return HttpResponseRedirect('/login /')


#edit user  forms
def Eadit_user_form(request):


   return render(request,'edit_form.html')

      