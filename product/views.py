from rest_framework import viewsets, filters

from .models import ProductType, PhysicalBook, EBook, AudioBook
from .serializers import ProductTypeSerializer, PhysicalBookSerializer, AudioBookSerializer, EBookSerializer


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class PhysicalBookViewSet(viewsets.ModelViewSet):
    queryset = PhysicalBook.objects.select_related('product_type').prefetch_related('categories').all()
    serializer_class = PhysicalBookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'author', 'translator', 'ISBN']
    filterset_fields = ['price', 'discount', 'stock', 'is_available']


class EBookViewSet(viewsets.ModelViewSet):
    queryset = EBook.objects.select_related('product_type').prefetch_related('categories').all()
    serializer_class = EBookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'author', 'translator', 'ISBN', 'file_format']
    filterset_fields = ['price', 'discount', 'stock', 'is_available']

class AudioBookViewSet(viewsets.ModelViewSet):
    queryset = AudioBook.objects.select_related('product_type').prefetch_related('categories').all()
    serializer_class = AudioBookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'author', 'narrator']
    filterset_fields = ['price', 'discount', 'stock', 'is_available']
