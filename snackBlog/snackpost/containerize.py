from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['title','content','timestamp','updated','author','published']
        model = Post
        