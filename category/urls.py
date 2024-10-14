from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GeneralCategoryViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'general-categories', GeneralCategoryViewSet)
router.register(r'', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
