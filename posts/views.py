from django.db import models
from django.shortcuts import render
from rest_framework.generics  import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.permissions  import IsAuthenticatedOrReadOnly
# from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer
from .models import Post
from .permissions import IsOwnerOrReadOnly

# generic views from rest framework
# not template views

class PostList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
