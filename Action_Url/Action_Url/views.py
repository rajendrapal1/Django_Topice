from django.http import HttpResponse,HttpResponseRedirect
from django .shortcuts import render,redirect



def Form_page(request):
    return render(request,'form.html')

def Action_method(request):  # action method all data redirect an other page or heet another url 
    # var=0
    # data={}
    # try:
    #     if request.method=='POST':
    #         D1=int(request.POST.get('ename'))
    #         D2=int(request.POST.get('ppass'))
    #     var=D1+D2
    #     print(var)
    #     data={
    #        'D1':D1,
    #        'D2':D2,
    #        'Total':var
    #     } 
    #     print(data)

        
    #     #  if request.method=="POST":
    #     #     p1=int(request.POST.get('num1'))
    #     #     p2=int(request.POST.get('num2')) 
    #     #     var=p1+p2
    #     #     print(var)
    #     #     data={
    #     #         'p1':p1,
    #     #         'p2':p2,
    #     #         'result':var
    #     #     }

    #     url="/formpage/?abc={}".format(data)

      
        return HttpResponse(request)

    
    #except:
       #print("try block not work")    
    

def Home_page(request):

    var=0;
    data={}
    try:
        # if request.method=="GET":
        #     p1=int(request.GET['num1'])
        #     p2=int(request.GET['num2'])
        #     var=p1+p2
        #     print(var)

         if request.method=="POST":
            p1=int(request.POST.get('num1'))
            p2=int(request.POST.get('num2'))
            var=p1+p2
            print(var)
            data={
                'p1':p1,
                'p2':p2,
                'result':var
            }

            url="/formpage/?abc={}".format(var)
            # return HttpResponseRedirect(url)   
            return redirect(url)
          
    except:
        pass        
    return render(request,'home.html',data)