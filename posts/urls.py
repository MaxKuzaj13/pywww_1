from .views import posts, ListPostView, DetailPostsView, CreatePostsView
from django.urls import path, include

app_name = "posts"

urlpatterns = [
    #path('', posts),
    path('list/', ListPostView.as_view(), name='list_view_post'),
    path('add/', CreatePostsView.as_view(), name='add_post'),
    path('<slug:pk>/', DetailPostsView.as_view(), name='detail_post_view'),

]

