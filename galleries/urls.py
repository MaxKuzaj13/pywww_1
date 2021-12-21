from .views import ListGalleryView, ListPhotoView, DetailPhotoView, CreateGalleryView, CreatePhotoView
from django.urls import path, include

app_name = "galleries"

urlpatterns = [
    #path('', posts),
    #path('list/', ListGalleryView.as_view(), name='gallery_list'),
    path('', ListGalleryView.as_view(), name='gallery_list'),
    path('add/',  CreateGalleryView.as_view(), name='gallery_add'),
    path('<slug:gallery_id>/', DetailPhotoView.as_view(), name='gallery_details'),
    path('<slug:gallery_id>/add/',  CreatePhotoView.as_view(), name='photo_add'),
]

