from rest_framework import serializers
from .models import GeneralCategory, Category


class GeneralCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralCategory
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'general_category', 'sub_parent', 'sub_categories']

    @staticmethod
    def get_sub_categories(obj):
        descendants = obj.get_descendants()
        return CategorySerializer(descendants, many=True).data