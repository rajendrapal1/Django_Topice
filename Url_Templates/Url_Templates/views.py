from django.shortcuts import render

def header_fun(request):
    return render(request,'header.html')

def footer_fun(request):
    return render(request,'footer.html')

def base_fun(request):
    return render(request,'base.html')

def index_fun(request):
    return render(request,'index.html')
def about_fun(request):
    return render(request,'about.html')
def main_fun(request):
    return render(request,'main.html')