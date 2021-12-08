from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

from .models import Gallery, Photo


class GalleryResource(resources.ModelResource):
    class Meta:
        model = Gallery

# admin.site.register(Post)

@admin.register(Gallery)
class PostAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'modified']
    # list_filter = ['published', 'sponsored']
    search_fields = ['title']
    # filter_horizontal = ['tags']
    resource_class = GalleryResource

class PhotoResource(resources.ModelResource):
    class Meta:
        model = Photo

@admin.register(Photo)
class PostAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'modified']
    # list_filter = ['published', 'sponsored']
    search_fields = ['title']
    # filter_horizontal = ['tags']
    resource_class = PhotoResource
