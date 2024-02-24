from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('create_profile/', views.CreateProfileView.as_view(), name='create_profile'),
]
