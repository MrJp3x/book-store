from rest_framework import serializers
from .models import ProductType, EBook, AudioBook, PhysicalBook


class BaseBookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')


class ProductTypeSerializer(BaseBookSerializer):
    class Meta:
        model = ProductType

class PhysicalBookSerializer(BaseBookSerializer):
    class Meta(BaseBookSerializer.Meta):
        model = PhysicalBook

class EBookSerializer(BaseBookSerializer):
    class Meta(BaseBookSerializer.Meta):
        model = EBook

class AudioBookSerializer(BaseBookSerializer):
    class Meta(BaseBookSerializer.Meta):
        model = AudioBook
