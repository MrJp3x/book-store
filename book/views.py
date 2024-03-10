from rest_framework.viewsets import ModelViewSet

from .models import Book, BookCategory, Author
from .serializers import BooksSerializer, BooksCategorySerializer, AuthorSerializer


class HandleBooks(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class HandleBookCategory(ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BooksCategorySerializer


class HandleAuthor(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
