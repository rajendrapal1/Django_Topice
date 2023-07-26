from django.shortcuts import render
from django.views.generic.edit import FormView
from app .forms import ContectForm
from django.views.generic.base import TemplateView
# Create your views here.

class Contect_Class_views(FormView):
    template_name ="app/contact.html"
    form_class =ContectForm
    
    success_url ="/Displaydata/"

class Display_Data(TemplateView):
    template_name="app/Display.html"

