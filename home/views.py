from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
# Create your views here.
class Home1(generic.View):
    def get(self,request, *args, **kwargs):
        return HttpResponse('Bienvenido ma nino')
class Home(generic.TemplateView):
    template_name="home/home.html"