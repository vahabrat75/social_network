from rest_framework import generics, status
from rest_framework.response import Response

from post.models import Like
from post.serializers import PostCreateSerializer, PostLikeSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class CreatePost(generics.CreateAPIView):
    """Create a post"""
    serializer_class = PostCreateSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = request.user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LikePost(generics.CreateAPIView):
    """Like and unlike a post"""
    serializer_class = PostLikeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        like = Like.objects.filter(user=request.user, post_id=request.data.get('post')).first()
        if like is None:
            like = Like.objects.create(user=request.user, post_id=request.data.get('post'), is_liked=True)
        else:
            like.is_liked = not like.is_liked
            like.save()

        headers = self.get_success_headers(serializer.data)
        data = {
            'post_id': like.post_id,
            'is_liked': like.is_liked
        }
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)