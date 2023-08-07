from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post,User,Like
from .serializers import UserSerializers,PostSerializers,LikeSerializers

# Create your views here.

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance=self.get_object()
        if instance.is_public or request.user== instance.owner:
            serializer=self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response({"details:You do not have permission to access this post."},status=403)

    def update(self, request, *args, **kwargs):
        instance=self.get_object()
        if instance.user !=instance.owner:
            return Response({"detail:You do not have the permission of update this post."},status=403)
        return super().update(request,*args,**kwargs)

    def destroy(self, request, *args, **kwargs):
        instance=self.get_object()
        if instance.user  != instance.owner:
            return Response({"detail:You do not have permission to delete this post."},status=403)
        return super().destroy(request,*args,**kwargs)

class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializers

class LikeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializers


