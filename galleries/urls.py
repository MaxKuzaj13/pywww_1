from .views import ListGalleryView, ListPhotoView
from django.urls import path, include

app_name = "galleries"

urlpatterns = [
    #path('', posts),
    path('list/', ListGalleryView.as_view(), name='gallery_list'),
    path('list/photo/', ListPhotoView.as_view(), name='photo_list'),
]

