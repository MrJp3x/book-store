import base64
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .forms import PasswordResetForm
from .serializers import (UserProfileSerializer, PublisherProfileSerializer, AdminProfileSerializer, RegisterSerializer)
from .models import (UserProfile, PublisherProfile, AdminProfile, User)


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


class BaseProfileView(APIView):
    """Base view for handling profile operations for different user types.

    Attributes:
        model (models.Model): The model class representing the profile type.
        serializer_class (serializers.Serializer): The serializer class for the profile type.
    """
    model = None
    serializer_class = None

    def post(self, request):
        """Handles creating a profile for the user if it does not already exist.

        Args:
            request (Request): The request object containing user and profile data.

        Returns:
            Response: A Response object containing success or error message.
        """
        # Ensure model and serializer_class are set
        if not self.model or not self.serializer_class:
            return Response({"error": "Model or serializer not set."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the profile already exists for the user
        if self.model.objects.filter(user=request.user).exists():
            return Response({"error": "Profile already exists"}, status=status.HTTP_400_BAD_REQUEST)

        # Validate and save the profile data
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        # Save the profile associated with the current user
        serializer.save(user=request.user)
        return Response({"data": "Profile is created."}, status=status.HTTP_201_CREATED)

    def get(self, request):
        """Handles retrieving the profile for the current user.

        Args:
            request (Request): The request object containing user information.

        Returns:
            Response: A Response object containing profile data or an error message.
        """
        # Ensure model and serializer_class are set
        if not self.model or not self.serializer_class:
            return Response({"error": "Model or serializer not set."}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve the profile associated with the current user
        profile = self.model.objects.filter(user=request.user).first()
        if not profile:
            return Response({"error": "User not exists"}, status=status.HTTP_400_BAD_REQUEST)

        # Serialize the profile data
        serializer = self.serializer_class(profile)
        return Response({"data": serializer.data})

    def put(self, request):
        """Handles updating the profile for the current user.

        Args:
            request (Request): The request object containing updated profile data.

        Returns:
            Response: A Response object containing the updated profile data or an error message.
        """
        # Ensure model and serializer_class are set
        if not self.model or not self.serializer_class:
            return Response({"error": "Model or serializer not set."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the profile exists for the user
        profile = self.model.objects.filter(user=request.user).first()
        if not profile:
            return Response({"error": "Profile not exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Validate and update the profile data
        serializer = self.serializer_class(profile, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data)


class UserProfileView(BaseProfileView):
    """View for handling operations related to the regular user profile."""
    model = UserProfile
    serializer_class = UserProfileSerializer


class PublisherProfileView(BaseProfileView):
    """View for handling operations related to the publisher profile."""
    model = PublisherProfile
    serializer_class = PublisherProfileSerializer


class AdminProfileView(BaseProfileView):
    """View for handling operations related to the admin profile."""
    model = AdminProfile
    serializer_class = AdminProfileSerializer

# endregion
