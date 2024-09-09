from django.db import models
from category.models import Category

# None
class Product(models.Model):
    name = models.CharField(max_length=100, unique=False, blank=False, null=False)
    # category = models.CharField(max_length=120, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(blank=False, null=False)
    discount = models.FloatField(blank=True, null=True, default=0)
    description = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True, default=0)



    def __str__(self):
        return f'{self.category} / {self.name} / {self.quantity}'
