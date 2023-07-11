from django.shortcuts import render
def Post_Data(request):
    var=0;
    dic={}
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
    except:
        pass    
    return render(request,'temp.html',data) 