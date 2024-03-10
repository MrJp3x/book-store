from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Book, BookCategory, Author


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BooksCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=BookCategory.objects.all(),
                fields=['category']
            )
        ]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        field = '__all__'
