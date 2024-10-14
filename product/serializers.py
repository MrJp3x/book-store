from rest_framework import serializers
from .models import ProductType, EBook, AudioBook, PhysicalBook


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class EBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = EBook
        fields = '__all__'


class AudioBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = '__all__'


class PhysicalBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalBook
        fields = '__all__'