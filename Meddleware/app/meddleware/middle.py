# functin base middleware

# def simple_middleware(get_response):
#     print("*********************************")
#     print("One-time configuration and initialization.")
#     print("*********************************")

#     def middleware(request):

#         print("*************************")
#         print("code will be excute befor views")
#         print("*********************************")

#         response = get_response(request)

#         print("after views")

#         return response

#     return middleware


# class based middleware
class Middilewate_class():
    def __init__(self,get_responce):
        self.get_responce=get_responce
        print("code one time will be excute befor meddleware")

    def __call__(self,request):

        print("befor views excute")
        print("***********************")

        responce=self.get_responce(request)
        print("vies function excute nex code")
        return responce
    
       
