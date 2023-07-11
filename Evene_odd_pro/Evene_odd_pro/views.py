from django.shortcuts import render

def home_page(request):
    save=0
    try:
        if request.method=='POST':
            if request.POST.get('num1')=="":
                return render(request,'home_page.html',{'err':True,})
            
            data1=eval(request.POST.get('num1'))
            if data1%2==0:
                save="even number"
            else:
                save="odd number"    
    except:
        pass        
    return render(request,'home_page.html',{'show':save})

#MARKSHEET
def marksheet(request):
    
    d=0
    try:
        if request.method=='POST':
            d1=int(request.POST.get('num1'))
            d2=int(request.POST.get('num2'))
            d3=int(request.POST.get('num3'))
            d4=int(request.POST.get('num4'))
            d5=int(request.POST.get('num5'))
            total=d1+d2+d3+d4+d5
            per=total*100/500
            if per>=30:
                d="Third Division"
            elif per>=40:
                d="second division"
            elif per>=60:
                d="first division"
            elif per<30:
                d="fale"            

            data={
                'total':total,
                'per':per,
                'd':d
            }
            return render (request,'marksheet.html',data)

    except:
        pass        
    return render(request,'marksheet.html')

# manual form balidation

def manual_forms(request):
    try:    
        if (request.method=="POST"):
             
             if request.POST.get('num1')=="":
                 
                 return render(request,'manual_forms.html',{'error':True,'msg':'plz enter a values'})
             

             d1= str(request.POST.get('num1'))
               
            # return render(request,'manual_forms.html',{'values1':d1})
            
  
    except:
        pass
    return render(request,'manual_forms.html',{'values1':d1})
