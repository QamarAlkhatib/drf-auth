from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from .containerize import PostSerializer
from .models import Post


class PostList(generics.ListAPIView):
    
    queryset = Post.objects.all()   
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()   
    serializer_class = PostSerializer
