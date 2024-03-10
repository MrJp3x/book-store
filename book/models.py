from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)
    phone = models.CharField(max_length=512, blank=True, null=True)
    address = models.CharField(max_length=512, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)


class BookCategory(models.Model):
    category = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.category


class Book(models.Model):
    name = models.CharField(max_length=512, unique=True)
    title = models.CharField(max_length=512)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(BookCategory)
    online_price = models.PositiveIntegerField()
    physical_price = models.PositiveIntegerField()
    online_pages_count = models.PositiveIntegerField()
    physical_pages_count = models.PositiveIntegerField()
    genre = models.CharField(max_length=512)
    ISBN = models.CharField(max_length=225, unique=True)
    description = models.TextField(max_length=2048, blank=True, null=True)
    number_of_publications = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    discount = models.PositiveIntegerField(blank=True, null=True)

