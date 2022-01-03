from django.contrib import admin
from .models import Health


@admin.register(Health)
class HealthAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'created', 'modified']
    # list_display = ['id', 'title', 'description', 'author', 'publication_year', 'created', 'modified', 'available']
    # search_fields = ['title', 'description', 'author']
    # list_filter = ['available']