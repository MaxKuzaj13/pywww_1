from .views import ListGalleryView, ListPhotoView, DetailPhotoView
from django.urls import path, include

app_name = "galleries"

urlpatterns = [
    #path('', posts),
    #path('list/', ListGalleryView.as_view(), name='gallery_list'),
    path('', ListGalleryView.as_view(), name='gallery_list'),
    path('<slug:gallery_id>/', DetailPhotoView.as_view(), name='gallery_details'),
]

