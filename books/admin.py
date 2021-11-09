from django.contrib import admin
from .models import BookModel


@admin.register(BookModel)
class BookModel(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'author', 'publication_year', 'created', 'modified', 'available']
    search_fields = ['title', 'description', 'author']
    list_filter = ['available']
