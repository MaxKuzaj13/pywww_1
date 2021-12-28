from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget, AdminURLFieldWidget
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from import_export import resources
from import_export.admin import ExportMixin
from sorl.thumbnail import get_thumbnail

from .models import Gallery, Photo
from django.db import models


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            print(value)
            t = get_thumbnail(value, "150")
            print(t.url)

            output.append(f'<a href="{value.url}" target="_blank"><img src="{t.url}"></a>')
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        output.append('<div>test</div>')
        #return mark_safe(u''.join(output))
        return u''.join(output)


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
    list_display = ['id', 'title', 'created', 'modified', 'image']
    # list_filter = ['published', 'sponsored']
    search_fields = ['title']
    # filter_horizontal = ['tags']
    resource_class = PhotoResource
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}



# admin.site.site_header = "PyWWW Admin"
# admin.site.site_title = "PyWWW Admin"
admin.site.index_title = "Witaj w Portalu PyWWW"