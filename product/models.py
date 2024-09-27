from django.db import models
from django.urls import reverse

from utils.models import TimeStamp


# region Product
class Product(TimeStamp):
    """
    Abstract base class representing a generic product with common fields.

    Attributes:
        name (models.CharField): The name of the product.
        price (models.FloatField): The price of the product.
        discount (models.FloatField): The discount on the product, if any.
        stock (models.PositiveIntegerField): The number of items available in stock.
        description (models.TextField): A detailed description of the product.
        rating (models.FloatField): The rating of the product.

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

# endregion


# region BookCategory
class BookCategory(models.Model):
    """
    Represents a category for products, such as Fiction, Non-Fiction, Accessories, etc.

     Attributes:
        name (models.CharField): The name of the category.
        slug (models.SlugField): A URL-friendly identifier for the category.

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

# endregion


# region Book
class Book(Product):
    """
    Represents a book product, inheriting from Product and adding specific fields.
    Acts as a parent class for specific types of books.

    Attributes:
        author (models.CharField): The author of the book.
        translator (models.CharField): The translator name of the book.
        publication_name (models.CharField): The publication name of the book.
        category (models.ForeignKey): The category to which the book belongs.
        slug (models.SlugField): A URL-friendly identifier for the book.
        cover_image (models.ImageField): The cover image of the book.
        ISBN (models.CharField): The ISBN number.
        subject (models.CharField): The subject of the book.

    """

    author = models.CharField(max_length=100, help_text="Author of the book")
    translator = models.CharField(max_length=100, blank=True, null=True)
    publication_name = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(BookCategory, related_name='books', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, help_text="URL-friendly identifier for the book")
    cover_image = models.ImageField(upload_to='book_covers/', help_text="Cover image of the book")
    ISBN = models.CharField(max_length=25, blank=True, null=True)
    subject = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the URL to access the detail view of the book.
        """
        return reverse('product:book_detail', args=[self.slug])

# endregion


# region PhysicalBook
class PhysicalBook(Book):
    """
    Represents a physical (hardcopy) book, inheriting from Book and adding specific fields.

    Attributes:
        weight (models.DecimalField): The weight of the book in kilograms.
        dimensions (models.CharField): The dimensions of the book (e.g., 8x11x2 inches).
        cover_type (models.CharField): The type of book cover.
        number_of_pages (models.PositiveIntegerField): The number of book pages.

    """

    weight = models.DecimalField(max_digits=5, decimal_places=2, help_text="Weight of the book in kilograms")
    dimensions = models.CharField(max_length=100, help_text="Dimensions of the book (e.g., 8x11x2 inches)")
    cover_type = models.CharField(max_length=50, blank=True, null=True)
    number_of_pages = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.name}"

# endregion


# region EBook
class EBook(Book):
    """
    Represents an electronic (e-book) product, inheriting from Book and adding specific fields.

     Attributes:
        FILE_FORMAT_CHOICES (tuple): Available file formats for the e-book.
        file_format (models.CharField): The file format of the e-book.
        download_url (models.URLField): The URL to download the e-book.
        file_size (models.DecimalField): The file size of the e-book in MB.
        number_of_pages (models.PositiveIntegerField): The number of book pages.

    """
    FILE_FORMAT_CHOICES = (
        ('pdf', 'PDF'),
        ('epub', 'EPUB'),
        ('mobi', 'MOBI'),
    )

    file_format = models.CharField(max_length=50, choices=FILE_FORMAT_CHOICES)
    download_url = models.URLField(help_text="URL to download the e-book")
    file_size = models.DecimalField(max_digits=6, decimal_places=2, help_text="File size in MB")
    number_of_pages = models.PositiveIntegerField(blank=False, null=False)

    def __str__(self):
        return f"E-Book: {self.name}"

# endregion


# region AudioBook
class AudioBook(Book):
    """
    Represents an audiobook product, inheriting from Book and adding specific fields.

    Attributes:
        audio_length (models.DurationField): The total length of the audiobook.
        narrator (models.CharField): The narrator of the audiobook.
        audio_url (models.URLField): The URL to listen to the audiobook.
        episode_count (models.PositiveIntegerField): The number of episodes in the audiobook.

    """
    audio_length = models.DurationField(help_text="Total length of the audio book")
    narrator = models.CharField(max_length=100)
    audio_url = models.URLField(help_text="URL to listen to the audio book")
    episode_count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"

# endregion