from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import ListHealthView, CreateHealthView

app_name = "health"

urlpatterns = [
    path('', ListHealthView.as_view(), name='health_list'),
    path('add/',  CreateHealthView.as_view(), name='health_add'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

