
from django .shortcuts import HttpResponse
#process based middleware
class Mymiddleware():

    def __init__(self,get_responce) :
        self.get_responce=get_responce
        # print("my middleware excute at once time ")
    def __call__(self,request):
    #    print("befor view excute")

       responce=self.get_responce(request)
    #    print("after views excute")
       return responce
    def process_view(request,*args,**kwargs):   # processview excute before viewsfunction
        # print("befor views")
        # return HttpResponse("this is processview")
        return None

# process exception middleware  //handle code of errors
class Process_Exception_Middleware():
    def __init__(self,get_responce) :
        self.get_responce=get_responce
    def __call__(self,request):
       responce=self.get_responce(request)
       return responce
   
    def process_exception(self,request,exeption):   # processview excute before viewsfunction
        ex=exeption
        return HttpResponse(ex)
        # return None

# Template Responce middleware

class Template_Responce_Middleware():
    def __init__(self,get_responce) :
        self.get_responce=get_responce

    def __call__(self,request):
       responce=self.get_responce(request)
       return responce
   
    def Template_Responce(self,request,responce):   
        responce.context_data['name'] ='RAJENDRA'
        print(responce)
        return responce
        # return None


