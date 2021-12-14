from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import Post
from .forms import PostForm
from django.conf import settings


def posts(request):
    return HttpResponse('posts')


def post_list(request):
    return HttpResponse('posts')


class ListPostView(ListView):
    paginate_by = 10
    model = Post
    template_name = 'posts/list_view.html'
    context_object_name = 'posts_list'


    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)

    def get_queryset(self):
        return Post.objects.filter(published=True).order_by('-pk')



class DetailPostsView(DetailView):
    model = Post
    template_name = 'posts/detail_view.html'
    context_object_name = 'detail_view_post'

    def get_queryset(self):
        return Post.objects.filter(published=True).order_by('-pk')


class CreatePostsView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/add.html'
    success_url = 'list'

