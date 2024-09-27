from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (RegisterView, LoginView,
                    UserProfileView, PublisherProfileView, AdminProfileView,
                    PasswordResetRequestAPIView, PasswordResetConfirmAPIView)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('password-reset/', PasswordResetRequestAPIView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmAPIView.as_view(), name='password_reset_confirm'),
    path('profile/user/', UserProfileView.as_view(), name='user_profile'),
    path('profile/publisher/', PublisherProfileView.as_view(), name='publisher_profile'),
    path('profile/admin/', AdminProfileView.as_view(), name='admin_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
