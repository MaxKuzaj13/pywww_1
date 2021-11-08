from .views import posts
from django.urls import path, include


urlpatterns = [
    path('', posts),

]

