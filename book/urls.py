from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HandleAuthor, HandleBookCategory, HandleBooks


router = DefaultRouter()
router.register(r'book', HandleBooks)
router.register(r'category', HandleBookCategory)
router.register(r'author', HandleAuthor)


urlpatterns = [
    path('', include(router.urls)),
]
