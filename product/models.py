from django.db import models
from django.urls import reverse

from utils.models import TimeStamp



class Product(TimeStamp):
    """
    Abstract base class representing a generic product with common fields.
    """
    name = models.CharField(max_length=100, unique=False, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    discount = models.FloatField(blank=True, null=True, default=0)
    stock = models.PositiveIntegerField(default=0, help_text="Number of items in stock")
    description = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)


    class Meta:
        # Enable multi-table inheritance
        abstract = False


    def __str__(self):
        return f'{self.name} / {self.stock} / {self.price}'

    def get_absolute_url(self):
        """
        Returns the URL to access the detail view of the product.
        """
        return reverse('product:product_detail', args=[self.id])


class BookCategory(models.Model):
    """
    Represents a category for products, such as Fiction, Non-Fiction, Accessories, etc.
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, help_text="URL-friendly identifier for the category")

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the URL to access a list of products in this category.
        """
        return reverse('product:product_list_by_category', args=[self.slug])



class Book(Product):
    """
    Represents a book product, inheriting from Product and adding specific fields.
    Acts as a parent class for specific types of books.
    """
    author = models.CharField(max_length=100, help_text="Author of the book")
    category = models.ForeignKey(BookCategory, related_name='books', on_delete=models.CASCADE,
                                 help_text="Category of the book")
    slug = models.SlugField(max_length=200, unique=True, help_text="URL-friendly identifier for the book")
    cover_image = models.ImageField(upload_to='book_covers/', help_text="Cover image of the book")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the URL to access the detail view of the book.
        """
        return reverse('product:book_detail', args=[self.slug])


class PhysicalBook(Book):
    """
    Represents a physical (hardcopy) book, inheriting from Book and adding specific fields.
    """
    weight = models.DecimalField(max_digits=5, decimal_places=2, help_text="Weight of the book in kilograms")
    dimensions = models.CharField(max_length=100, help_text="Dimensions of the book (e.g., 8x11x2 inches)")

    def __str__(self):
        return f"{self.name}"


class EBook(Book):
    """
    Represents an electronic (e-book) product, inheriting from Book and adding specific fields.
    """
    FILE_FORMAT_CHOICES = (
        ('pdf', 'PDF'),
        ('epub', 'EPUB'),
        ('mobi', 'MOBI'),
    )

    file_format = models.CharField(max_length=50, choices=FILE_FORMAT_CHOICES)
    download_url = models.URLField(help_text="URL to download the e-book")
    file_size = models.DecimalField(max_digits=6, decimal_places=2, help_text="File size in MB")

    def __str__(self):
        return f"E-Book: {self.name}"


class AudioBook(Book):
    """
    Represents an audiobook product, inheriting from Book and adding specific fields.
    """
    audio_length = models.DurationField(help_text="Total length of the audio book")
    narrator = models.CharField(max_length=100)
    audio_url = models.URLField(help_text="URL to listen to the audio book")
    episode_count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"

