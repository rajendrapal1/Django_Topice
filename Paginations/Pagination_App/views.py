from django.shortcuts import render
from Pagination_App .models import Model_class
from django.core.paginator import Paginator
from django.core.mail import send_mail

# Create your views here.
def Show_page(request):
    data=Model_class.objects.all() # GET ALL FIELD OF DATA 
    paginator = Paginator(data,1) # WE ARE GIVE THE LIMIN OF PAGE
    page = request.GET.get('page') # GET DATA FROM URL 
    posts = paginator.get_page(page) #
    totalpage=posts.paginator.num_pages
    alldata=[n+1 for n in range(totalpage)]
    print(alldata)
    data1={'dt':posts,
           'total':totalpage,
           'all_data':alldata
           }
    
    # send_mail(
    #     "POST OF PYTHON DEVELOPER",
    #     "I am looking job python developers",
    #     "rajendra.ai242@gmail.com",
    #     ["rajendra.ai121@gmail.com"],
    #     fail_silently=False,
    # )
    
    return render(request,'homepage.html',data1)

def Gemail_fun(request):

        send_mail(
            "Post of Python Developers",
            "I got your mail nokari.com  ",
            "mm3@3m-technology.com",
            ["rajendra.ai121@gmail.com"],
            fail_silently=False,
    )