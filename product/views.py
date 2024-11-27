from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import ProductType, PhysicalBook, EBook, AudioBook
from .serializers import ProductTypeSerializer, PhysicalBookSerializer, AudioBookSerializer, EBookSerializer
from utils.product_search_filter import BookFilter, PhysicalBookFilter, EBookFilter, AudioBookFilter


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class BaseBookViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['name', 'author', 'description']
    ordering_fields = ['price', 'rating', 'created_at']
    ordering = ['created_at']

    def get_queryset(self):
        return self.queryset.select_related('product_type').prefetch_related('categories').all()

class PhysicalBookViewSet(BaseBookViewSet):
    queryset = PhysicalBook.objects.all()
    serializer_class = PhysicalBookSerializer
    filterset_class = PhysicalBookFilter

class EBookViewSet(BaseBookViewSet):
    queryset = EBook.objects.all()
    serializer_class = EBookSerializer
    filterset_class = EBookFilter
    search_fields = BaseBookViewSet.search_fields + ['file_format']


class AudioBookViewSet(BaseBookViewSet):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer
    filterset_class = AudioBookFilter
    search_fields = BaseBookViewSet.search_fields + ['narrator']