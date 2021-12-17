from django.shortcuts import get_object_or_404
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
        # return Gallery.objects.order_by('-pk')
        galleries = Gallery.objects.filter(status='published')
        # count sprawdza wszsytkie i robi wiele zapytan
        galleries = [g for g in galleries if g.photos.count() > 0]
        return galleries


# class DetailPhotoView(DetailView):
#     model = Gallery
#     template_name = 'galleries/photo_detail.html'
#     context_object_name = 'details'

    #
    # def get_queryset(self):
    #     # id = self.kwargs.get("pk")
    #     # print(pk)
    #     gallery = Photo.objects.order_by('gallery__title', '-pk')
    #     return gallery


class DetailPhotoView(DetailView):
    model = Gallery
    template_name = 'galleries/photo_detail.html'
    #context_object_name = 'details'

    def get_object(self, queryset=None):
        gallery = get_object_or_404(Gallery, pk=self.kwargs['gallery_id'])
        return gallery

    # def get_queryset(self):
    #     gallery_id=self.kwargs.get('gallery_id')
    #     print(gallery_id)
    #     gal = Gallery.objects.get(id=gallery_id)
    #     return gal
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

class ListPhotoView(ListView):
    paginate_by = 10
    model = Photo
    template_name = 'galleries/photo_list_view.html'
    context_object_name = 'photo_list'

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)

    def get_queryset(self):
        return Photo.objects.order_by('gallery__title', '-pk')