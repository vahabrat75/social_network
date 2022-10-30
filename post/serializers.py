from rest_framework import serializers
from post.models import Post, Like


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
                  'title',
                  'description',
                  'image',
                  'slug',
                  )


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
                  'post',
                  )