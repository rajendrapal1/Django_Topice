from django.shortcuts import render
from django.core.mail import send_mail 
from django.core.mail import EmailMultiAlternatives

# Create your views here.

def Send_Data(request):

   

    send_mail(
        "Python Devlopers",  # subject here 
        "i am working team opine solutions.", # messages
        "mm3@3m-technology.com", # sender mail
        ["rajendra.ai121@gmail.com"], # reseive
        fail_silently=False,
    )


#multialternative functions
def Email_fun(request):

    subject, from_email, to = "hello", "mm3@3m-technology.com", "rajendra.ai121@gmail.com"
    text_content = "This is an important message."
    html_content = "<p>This is an <strong>important</strong> message.</p>"
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html") #type deside
    msg.send()    