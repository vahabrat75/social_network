from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from post.models import Like
from user.models import RequestLog, User


class LikeListView(generics.ListAPIView):
    """Returns likes quantity for each post"""

    def list(self, request, *args, **kwargs):

        queryset = Like.objects.filter(is_liked=True)
        if self.request.query_params.get('date_from', None):
            queryset = queryset.filter(creation_date__gte=self.request.query_params.get('date_from'))

        if self.request.query_params.get('date_to', None):
            queryset = queryset.filter(creation_date__lte=self.request.query_params.get('date_to'))

        if self.request.query_params.get('post_id', None):
            queryset = queryset.filter(post_id=self.request.query_params.get('post_id'))

        data = {}
        for item in queryset:
            data[item.post_id] = 0
        # count likes for each post
        for item in queryset:
            data[item.post_id] += 1

        return Response(data)


class UserRequestInfoView(generics.RetrieveAPIView):
    """Returns last login and last request time for user"""
    def retrieve(self, request, *args, **kwargs):

        if self.request.query_params.get('user_id', None):
            last_request = RequestLog.objects.filter(user_id=self.request.query_params.get('user_id')).order_by('-created').first()
            user = get_object_or_404(User, id=self.request.query_params.get('user_id'))
            to_resp = {
                'last_login': user.last_login,
                'last_request': last_request.created if last_request is not None else 'No requests were made.',
            }
            return Response(to_resp)
        else:
            return Response("Missing 'user_id' query parameter!", status=403)
