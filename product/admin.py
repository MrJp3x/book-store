from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'quantity']
    search_fields = ['name']
    list_filter = ['category', 'price']


admin.site.register(Product, ProductAdmin)
