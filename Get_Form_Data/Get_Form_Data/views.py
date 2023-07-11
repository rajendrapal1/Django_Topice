from django.shortcuts import render
def Get_fun(request):
    data=0;
    try:
        n1= int(request.GET['num1'])
        n2= int(request.GET['num2'])
        print(n1+n2)
          
        #   P1=request.POST['num1']
        #   P2=request.POST['num2']
        #   print(P1+P2)

        data=n1+n2
    except:
        pass    
        print("error occur")
    return render(request,'tmp.html',{'data1':data})