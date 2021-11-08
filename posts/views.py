from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import Post


def posts(request):
    return HttpResponse('posts')

def post_list(request):
    return HttpResponse('posts')


class ListView(ListView):
    model = Post
    template_name = 'posts/list_view.html'
    context_object_name = 'posts_list'

class DetailView(DetailView):
    model = Post
    template_name = 'posts/detail_view.html'
    context_object_name = 'detail_view'





