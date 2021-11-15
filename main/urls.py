from .views import hello_world, HW
from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('about/', views.HW.as_view(), name='about'),

]

