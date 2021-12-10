from .views import ListGalleryView
from django.urls import path, include

app_name = "galleries"

urlpatterns = [
    #path('', posts),
    path('list/', ListGalleryView.as_view(), name='gallery_list'),
]

