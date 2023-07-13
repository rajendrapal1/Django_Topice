from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm  ,UserChangeForm

#user forms

class User_forms(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        # fields='__all__'


class edit_user_form(UserChangeForm) :  
    password=None
    class  Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login']
        
    
