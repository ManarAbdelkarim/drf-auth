from django.db import models
from django.shortcuts import render
from rest_framework  import generics
from rest_framework.permissions  import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer
from .models import Post

# generic views from rest framework
# not template views

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer



