from django.shortcuts import render
from APP_Redirect. forms import StudentRegistations
from django.http import HttpResponseRedirect
# Create your views here.
def Student_data(request):
    if request.method=='POST':
        n=StudentRegistations(request.POST)
        data=n.is_valid() # return true or false 

        N=n.cleaned_data['name']
        E=n.cleaned_data['email']
        P=n.cleaned_data['password']
        print(N)
        print(E)
        print(P)

        

        
        
        
        return render(request,'Showdata.html',{'dt':N})
        return HttpResponseRedirect('/show/')
    else:
        n=StudentRegistations()
    return render(request,'homepage.html',{'dt':n})

def showdata(request):
    return render(request,'Showdata.html')