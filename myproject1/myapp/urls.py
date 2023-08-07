from django.urls import path
from .views import (
    UserListCreateView,UserRetrieveUpdateDeleteView,
    PostListCreateView,PostRetrieveUpdateDeleteView,
    LikeListCreateView,LikeRetrieveUpdateDeleteView,
)

urlpatterns=[
    path('users/',UserListCreateView.as_view(),name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDeleteView.as_view(), name='user-retrieve-update-delete'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDeleteView.as_view(), name='post-retrieve-update-delete'),
    path('likes/', LikeListCreateView.as_view(), name='like-list-create'),
    path('likes/<int:pk>/', LikeRetrieveUpdateDeleteView.as_view(), name='like-retrieve-update-delete'),
]
