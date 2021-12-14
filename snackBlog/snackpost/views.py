from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from .containerize import PostSerializer
from .models import Post
from .permissions import IsAuthenticatedOrReadOnly

class PostList(generics.ListCreateAPIView):
    permission_class = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()   
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_class = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()   
    serializer_class = PostSerializer
