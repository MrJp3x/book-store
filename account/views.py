from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Profile
from .serializers import RegisterSerializer, ProfileSerializer


class Register(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        serializer.save()
        return Response({'detail': 'User registered.'}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        if not user:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class ProfileView(APIView):
    def post(self, request):
        if Profile.objects.filter(user=request.user).exists():
            return Response({"error": "Profile already exists"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProfileSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"error": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(user=request.user)
        return Response({"data": "Profile is created."}, status=status.HTTP_201_CREATED)

    def get(self, request):
        profile = Profile.objects.filter(user=request.user).exists()
        if not profile:
            return Response({"error": "User not exists"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProfileSerializer(profile)
        return Response({"data": serializer.data})

    def put(self, request):
        profile = Profile.objects.filter(user=request.user)
        if not profile:
            return Response({"error": "Profile not exists."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)

        if not serializer.is_valid():
            return Response({"error": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data)
