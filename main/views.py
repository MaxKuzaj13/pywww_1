from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import TemplateView

def hello_world(request):
    templates = loader.get_template('main/about.html')
    return HttpResponse(templates.render())

class HW(TemplateView):
    template_name = 'main/about.html'
