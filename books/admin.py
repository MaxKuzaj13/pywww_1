from django.contrib import admin

# Register your models here.
from .models import BookModel

admin.site.register(BookModel)
