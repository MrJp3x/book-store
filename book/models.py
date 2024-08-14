from django.db import models
from product.models import Product
from category.models import Category


class Book(Product):
    # name = models.CharField(max_length=120, unique=False, blank=False, null=False)
    author = models.CharField(max_length=50, unique=False, blank=False, null=False)
    translator = models.CharField(max_length=50, blank=True, null=True)
    publisher = models.CharField(max_length=50, blank=True, null=True)
    ISBN = models.CharField(max_length=25, blank=True, null=True)
    subject = models.CharField(max_length=50, blank=True, null=True)
    book_size = models.CharField(max_length=50, blank=True, null=True)
    cover_type = models.CharField(max_length=50, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    number_of_pages = models.IntegerField(blank=False, null=False)
