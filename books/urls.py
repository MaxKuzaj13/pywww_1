from .views import books
from django.urls import path, include
from . import views

urlpatterns = [
    path('', books),
    path('list/', views.ListView.as_view(), name='list_view'),
    path('<slug:pk>/', views.DetailView.as_view(), name='detail_view'),
]