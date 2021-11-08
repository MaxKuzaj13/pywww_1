from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def posts(request):
    return HttpResponse('posts')