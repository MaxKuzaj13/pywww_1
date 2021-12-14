from .views import posts, ListPostView, DetailPostsView, CreatePostsView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = "posts"

urlpatterns = [
    #path('', posts),
    path('list/', ListPostView.as_view(), name='list_view_post'),
    path('add/', CreatePostsView.as_view(), name='add_post'),
    path('<slug:pk>/', DetailPostsView.as_view(), name='detail_post_view'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

