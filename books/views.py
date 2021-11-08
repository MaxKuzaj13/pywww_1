from django.shortcuts import render
from django.http import HttpResponse
from .models import BookModel

# def books(request):
#     return HttpResponse('books')

def books(request):
    books = BookModel.objects.all()
    return render(request, 'books/books.html', {'books':books})