from django.shortcuts import render 
from Bolock_App .models import Blog 
from django.http import HttpResponseRedirect 
from django.contrib import messages #import messages


#updat data from model form

# relative import of forms
def Edit_Page (request,id):
    if request.method == "GET":
         obj =Blog.objects.filter(id=id).first()
         print(obj) 
         if obj:
            return render(request, "Eadit_page.html",{'DT':obj})
            messages.success(request, "Message successful." )
         
    if request.method=="POST":
        # print(request.POST)
        title = request.POST.get('Title')

        discription = request.POST.get('Discription')

        imgs=request.POST.get('Img')
        # print(imgs)
        date = request.POST.get('release_date')
        # print(title,discription , date)

        obj=Blog.objects.filter(id=id).first()
        print(obj)
        if obj:
            print(obj.Title)
            print(obj.Discription)
            obj.Title = title
            obj.Discription = discription
            obj.Img = imgs
            obj.save()
            # return [obj.Title , obj.Discription]
            messages.success(request, "Successful Updata data ." )

        return render(request, "edit_res.html",)
        # return render HttpResponseRedirect()
    
   
    

#create data
def Creat_Page(request):
    if request.method=="POST":
        Tit=request.POST.get('tit')
        Dis=request.POST.get('dis')
        img=request.POST.get('imges')
        dat=request.POST.get('dt')
        dada=Blog(Title=Tit,Discription=Dis,Img=img)
        dada.save()


    return render(request,'Creat_page.html')



#show data in home page 
def Blog_Page(request):
    data=Blog.objects.all().order_by('-release_date').values()
    get_id=request.GET.get('id')
    # print(get_id)
    alldata={
        'dt':data,
         
    }
    return render(request,'Blog_page.html',alldata)

#Delete  data from models field
def Delete_page(request,id):
    if request.method=="POST":
    #    data=Blog.objects.get(id=id)
        data=Blog.objects.filter(id=id)
        print(data)
        data.delete()
    return HttpResponseRedirect('/blogpage/')   
       

    

# def Edit_Page(request,id):
#     if request.method=="POST":
#         data=Blog.objects.filter(id=id)
#         dt=Blog_Page(request=='POST', isinstance=(data))
        
#     return render(request,'Eadit_page.html',)




      