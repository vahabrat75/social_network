from rest_framework import generics, status
from rest_framework.response import Response

from user.serializers import UserRegisterSerializer


class RegisterUser(generics.CreateAPIView):

    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response("User successfully registered!", status=status.HTTP_201_CREATED, headers=headers)