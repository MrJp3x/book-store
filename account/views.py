from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer


class Register(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        serializer.save()
        return Response({'detail': 'User registered.'}, status=status.HTTP_201_CREATED)



