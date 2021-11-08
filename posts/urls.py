from .views import posts, ListView
from django.urls import path, include
from . import views


urlpatterns = [
    path('', posts),
    path('list/', views.ListView.as_view(), name='list_view'),
    path('<slug:pk>/', views.DetailView.as_view(), name='detail_view'),

]

