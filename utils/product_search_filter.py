import django_filters
from django_filters import rest_framework as filters
from rest_framework.exceptions import ValidationError

from product.models import Product, Book, PhysicalBook, EBook, AudioBook



class PositiveNumberFilter(django_filters.NumberFilter):
    def filter(self, qs, value):
        if value is not None and value < 0:
            raise ValidationError({"detail": "The value cannot be negative."})
        return super().filter(qs, value)


class BaseProductFilter(filters.FilterSet):
    min_price = PositiveNumberFilter(field_name="price", lookup_expr="gte")
    max_price = PositiveNumberFilter(field_name="price", lookup_expr="lte")
    price_range = django_filters.RangeFilter(field_name="price")
    min_discount = PositiveNumberFilter(field_name="discount", lookup_expr='gte')
    stock = PositiveNumberFilter(field_name="stock")
    stock_range = django_filters.RangeFilter(field_name="stock")
    is_available = django_filters.BooleanFilter(field_name="is_available")

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'min_discount', 'stock', 'is_available']


class BookFilter(BaseProductFilter):
    category = django_filters.CharFilter(field_name="categories__name", lookup_expr="icontains")

    class Meta(BaseProductFilter.Meta):
        model = Book
        fields = BaseProductFilter.Meta.fields + ['category']


class PhysicalBookFilter(BookFilter):
    class Meta(BookFilter.Meta):
        model = PhysicalBook
        fields = BookFilter.Meta.fields + ['cover_type']

class EBookFilter(BookFilter):
    class Meta(BookFilter.Meta):
        model = EBook
        fields = BookFilter.Meta.fields + ['file_format']

class AudioBookFilter(BookFilter):
    class Meta(BookFilter.Meta):
        model = AudioBook
        fields = BookFilter.Meta.fields + ['narrator']