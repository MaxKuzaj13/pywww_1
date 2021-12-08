from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import Gallery



class ListGalleryView(ListView):
    paginate_by = 10
    model = Gallery
    template_name = 'galleries/gallery_list_view.html'
    context_object_name = 'gallery_list'

    def get_queryset(self):
        return Gallery.objects.order_by('-pk')