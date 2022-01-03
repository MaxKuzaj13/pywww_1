from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.core.paginator import Paginator
from .forms import PhotoForm, GalleryForm
from django.db.models import Avg, Min, Max, Count
from .models import Gallery, Photo


class ListGalleryView(ListView):
    paginate_by = 10
    page = 1
    model = Gallery
    template_name = 'galleries/gallery_list_view.html'
    context_object_name = 'gallery_list'

    def get_queryset(self):
        galleries = Gallery.objects.filter(status='published').annotate(p_count=Count('photos')).filter(p_count__gt=0)
        # count sprawdza wszsytkie i robi wiele zapytan
        # galleries = Gallery.objects.filter(status='published')
        # galleries = [g for g in galleries if g.photos.count() > 0]

        return galleries

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)

    def get_page(self, queryset):
        return self.request.GET.get("page", self.page)


class DetailPhotoView(DetailView):
    model = Gallery
    paginate_by = 10
    page = 1
    template_name = 'galleries/photo_detail.html'
    #context_object_name = 'details'

    def get_object(self, queryset=None):
        gallery = get_object_or_404(Gallery, pk=self.kwargs['gallery_id'])
        return gallery

    def get_page(self, queryset):
        return self.request.GET.get("page", self.page)

class ListPhotoView(ListView):
    paginate_by = 10
    page = 1
    model = Photo
    template_name = 'galleries/photo_list_view.html'
    context_object_name = 'photo_list'

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)

    def get_page(self, queryset):
        return self.request.GET.get("page", self.page)


    def get_queryset(self):
        #photo = [g for g in photo if g.photos.count() > 0]
        return Photo.objects.order_by('gallery__title', '-pk')


class CreatePhotoView(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'galleries/add_photo.html'
    # success_url = ''

    def form_valid(self, form):
        if form.is_valid():
            photo = form.save(commit=False)
            gallery = get_object_or_404(Gallery, pk=self.kwargs['gallery_id'])
            photo.gallery = gallery
            form.save()
        return HttpResponseRedirect(reverse('galleries:photo_add', args=(gallery.id, )))

    def get_object(self, queryset=None):
        gallery = get_object_or_404(Photo, pk=self.kwargs['gallery_id'])
        return gallery


class CreateGalleryView(CreateView):
    model = Gallery
    form_class = GalleryForm
    template_name = 'galleries/add_gallery.html'

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('galleries:photo_add', args=(self.object.id,))