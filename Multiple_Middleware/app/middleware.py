from django.http import HttpResponse
# def Myfun_middleware(get_responce):

#     print("****************************************")
#     print("one time code will be excute")
#     print("*****************************************")

#     def middle(request):
#         print("****************************")
#         print("excurer code inside middle ware ")
#         print("****************************")
#         responce=get_responce(request)
#         print("after her view function excute")

#         return responce
    
#     return middle



class Brothermiddleware():
    def __init__(self,get_responce) :
        self.get_responce=get_responce
        print("************************")
        print("one time coge excute brother")
        print("************************")

    def __call__(self,request) :
        print(" Brother  meddleware code excute before_views")
        responce=self.get_responce(request)
        print(" Brother meddleware code excute After_views")
        print(responce)
        

        return responce
         
class Fathermiddleware():
    def __init__(self,get_responce):
        self.get_responce=get_responce
        print("Father middleware code one time excute ")

    def __call__(self,request):
        print("Father meddleware code excute before_views")
        # responce=HttpResponse("Brack next code")            # next middleware not excuted
        responce=self.get_responce(request)
        print("Father meddleware code excute after views",)

        return responce
    

         
class Mothermiddleware():
    def __init__(self,get_responce):
        self.get_responce=get_responce
        print("Mother middleware code one time excute ")

    def __call__(self,request):
        print("Mother meddleware code excute befor_eviews")
        responce=self.get_responce(request)   
        print("Mother meddleware code excute after _views",)

        return responce

