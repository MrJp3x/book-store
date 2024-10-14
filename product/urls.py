from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductTypeViewSet, PhysicalBookViewSet, EBookViewSet, AudioBookViewSet


router = DefaultRouter()
router.register(r'product-types', ProductTypeViewSet)
router.register(r'physical-books', PhysicalBookViewSet)
router.register(r'e-books', EBookViewSet)
router.register(r'audio-books', AudioBookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
