from .views import LikePostView, PostViewSet
from django.urls import path

urlpatterns = [
    path('add/', PostViewSet.as_view(), name='add-post'),    
    path('like/<str:post_id>', LikePostView.as_view(), name='like-post'),
]
