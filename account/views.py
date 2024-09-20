import base64
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from rest_framework import generics, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, ProfileSerializer
from .forms import PasswordResetForm
from .models import Profile, User


# region login register

class RegisterView(generics.CreateAPIView):
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


# endregion


# region password reset

class PasswordResetRequestAPIView(APIView):
    def post(self, request, *args, **kwargs):
        form = PasswordResetForm(request.data)
        if not form.is_valid():
            return Response({'detail': 'Invalid data.'}, status=status.HTTP_400_BAD_REQUEST)

        email = form.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            user_id = user.id

            uid_bytes = str(user_id).encode('utf-8')
            uidb64 = base64.b64encode(uid_bytes).decode('utf-8')

            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)

            return Response({'uidb64': uidb64, 'token': token, }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'detail': 'User not found. Redirect to register.'}, status=status.HTTP_404_NOT_FOUND)


class PasswordResetConfirmAPIView(APIView):
    def post(self, request, uidb64, token, *args, **kwargs):
        try:
            user_id = urlsafe_base64_decode(uidb64).decode('utf-8')
            user = User.objects.get(id=user_id)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({'detail': 'User not found. Redirect to register.'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the token is valid
        token_generator = PasswordResetTokenGenerator()
        if not token_generator.check_token(user, token):
            return Response({'detail': 'Invalid or expired token.'}, status=status.HTTP_400_BAD_REQUEST)

        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        if new_password != confirm_password:
            return Response({'detail': 'Passwords do not match!'}, status=status.HTTP_400_BAD_REQUEST)

        user.password = make_password(new_password)
        user.save()
        # TODO: Redirect to login page
        return Response({'detail': 'Password updated successfully.'})


# endregion


# region profile


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

# endregion
