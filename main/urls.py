from .views import hello_world, HW
from django.urls import path, include
from . import views



urlpatterns = [
    path('', hello_world),
    path('about/', views.HW.as_view()),

]

