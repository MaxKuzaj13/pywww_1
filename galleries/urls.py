from .views import ListGalleryView
from django.urls import path, include

app_name = "posts"

urlpatterns = [
    #path('', posts),
    path('list/', ListGalleryView.as_view(), name='list_view_gallery'),
]

