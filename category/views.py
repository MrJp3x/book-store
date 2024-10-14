from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import GeneralCategory, Category
from .serializers import GeneralCategorySerializer, CategorySerializer


class GeneralCategoryViewSet(viewsets.ModelViewSet):
    queryset = GeneralCategory.objects.all()
    serializer_class = GeneralCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def ancestors(self, request, pk=None):
        category = self.get_object()
        ancestors = category.get_ancestors()
        serializer = self.get_serializer(ancestors, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def descendants(self, request, pk=None):
        category = self.get_object()
        descendants = category.get_descendants()
        serializer = self.get_serializer(descendants, many=True)
        return Response(serializer.data)
