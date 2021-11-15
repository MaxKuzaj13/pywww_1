from django.shortcuts import render
from django.http import HttpResponse
from .models import BookModel
from django.views.generic import TemplateView, CreateView, ListView, DetailView


# def books(request):
#     return HttpResponse('books')

def books(request):
    books = BookModel.objects.all()
    return render(request, 'books/books.html', {'books': books})


class ListView(ListView):
    model = BookModel
    template_name = 'books/list_view.html'
    context_object_name = 'books_list'


class DetailView(DetailView):
    model = BookModel
    template_name = 'books/detail_view.html'
    context_object_name = 'detail_view_books'
