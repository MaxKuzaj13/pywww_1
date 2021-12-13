from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic.list import MultipleObjectMixin

from .models import Gallery, Photo


class ListGalleryView(ListView):
    paginate_by = 10
    model = Gallery
    template_name = 'galleries/gallery_list_view.html'
    context_object_name = 'gallery_list'

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)

    def get_queryset(self):
        return Gallery.objects.order_by('-pk')


class ListPhotoView(ListView):
    paginate_by = 10
    model = Photo
    template_name = 'galleries/photo_list_view.html'
    context_object_name = 'photo_list'

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)

    def get_queryset(self):
        return Photo.objects.order_by('gallery__title', '-pk')