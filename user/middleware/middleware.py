from rest_framework_simplejwt.exceptions import TokenError

from user.models import RequestLog, User
from rest_framework_simplejwt.tokens import AccessToken
from django.core.exceptions import PermissionDenied


class RequestCustomMiddleware:

    def __init__(self, get_response):
        """
        One-time configuration and initialisation.
        """
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        data = {
            'ip': request.META.get('REMOTE_ADDR'),
            'user_agent': request.META.get('HTTP_USER_AGENT'),
            'path': request.path,
            'request_method': request.method
        }

        access_header = request.META.get('HTTP_AUTHORIZATION', None)

        if access_header is not None:
            prefix, access_token = access_header.split(' ')
            try:
                access_token_obj = AccessToken(access_token)
            except TokenError:
                raise PermissionDenied
            user_id = access_token_obj['user_id']
            user = User.objects.get(id=user_id)
            data['user'] = user

        # add request info to the db
        RequestLog.objects.create(**data)

        return None
