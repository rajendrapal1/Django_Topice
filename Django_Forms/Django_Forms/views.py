from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from Wscubetech.forms import forms_class

def form_method(request):
    fm1=forms_class()

    show={'form':fm1}
    # try:
        

    
    #   if request.method=="POST": 
    #        Data1=request.POST('name'),
    #        Data2=request.POST('email'),
    #        Data3=request.POST(' password'),
    #        var={'name':Dat}
           

    # except:
    #     pass;       
        

    return render(request,'home.html',show)





# def form_method(request):
#     # if this is a POST request we need to process the form data
#     if request.method == "POST":
#         # create a form instance and populate it with data from the request:
#         form = forms_class(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect("/thanks/")

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = forms_class()

#     return render(request, "home.html", {"form": form})



#########################################################################
# calculator
def calculate(request):
    c=0
    try :
        if request.method=='POST':
            D1=eval(request.POST.get('num1'))
            D2=eval(request.POST.get('num2'))

            opr=request.POST.get('opr')
            
            if opr== '+' :
                c=D1+D2
            elif opr=='-':
                c=D1-D2
            elif opr=='*':
                c=D1*D2
            elif opr=='/':
                c=D1/D2            
    except:
        print('error')
        



    return render (request,'calculate.html',{'c':c})
