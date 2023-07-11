from django.shortcuts import render

def Base_fun(request):
    return render(request,'temp/base.html')

def header_fun(request):
    return render(request,'temp/heder.html')

def footer_fun(request):
    return render(request,'temp/footer.html')

def aboutus_fun(request):
    return render(request,'temp/aboutus.html')
