from django.shortcuts import render

from django.views.generic.list import ListView
from app .models import GenericView_List


# Create your views here.

class GeneriViews(ListView):

    model=GenericView_List
    # ordering=['name']
    ordering=['city']
    
