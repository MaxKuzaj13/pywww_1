from .views import hello_world
from django.urls import path, include


urlpatterns = [
    path('', hello_world),

]

