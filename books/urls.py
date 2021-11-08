from .views import books
from django.urls import path, include


urlpatterns = [
    path('', books),

]