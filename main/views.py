from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import TemplateView

def hello_world(request):
    template_name = 'main/main.html'
    return render(request, template_name)

class HW(TemplateView):
    template_name = 'main/about.html'
