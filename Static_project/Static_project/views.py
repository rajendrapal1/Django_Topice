from django.shortcuts import render
def static_fun(request):
    return render(request,'temp.html')