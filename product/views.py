from rest_framework import viewsets, filters

from .models import ProductType, PhysicalBook, EBook, AudioBook
from .serializers import ProductTypeSerializer, PhysicalBookSerializer, AudioBookSerializer, EBookSerializer


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class BaseBookViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['price', 'discount', 'stock', 'is_available']

    def get_queryset(self):
        return self.queryset.select_related('product_type').prefetch_related('categories').all()

class PhysicalBookViewSet(BaseBookViewSet):
    queryset = PhysicalBook.objects.all()
    serializer_class = PhysicalBookSerializer
    search_fields = ['name', 'author', 'translator', 'ISBN']

class EBookViewSet(BaseBookViewSet):
    queryset = EBook.objects.all()
    serializer_class = EBookSerializer
    search_fields = ['name', 'author', 'translator', 'ISBN', 'file_format']

class AudioBookViewSet(BaseBookViewSet):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer
    search_fields = ['name', 'author', 'narrator']