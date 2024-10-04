from django.db import models


class GeneralCategory(models.Model):
    """
     Represents a general category in the system.

    Attributes:
        name (str): The name of the general category.
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Category(models.Model):
    """
    Represents a category in the system.

    Attributes:
        name (str): The name of the category.
        description (str, optional): A brief description of the category. Defaults to None.
        general_category (GeneralCategory): The associated general category for this category.
        sub_parent (Category, optional): The parent category, used for nested categories. Defaults to None.
    """

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    general_category = models.ForeignKey(GeneralCategory, on_delete=models.CASCADE)
    sub_parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_categories')

    def __str__(self):
        return f'{self.name}'

    def get_ancestors(self):
        """
        Retrieves the list of ancestor categories for the current category.

        Iterates through the parent categories using the sub_parent field.

        Returns:
            list: A list of ancestor Category objects, ordered from root to the current category.
        """

        ancestors = []
        category = self
        while category.sub_parent:
            ancestors.insert(0, category.sub_parent)
            category = category.sub_parent
        return ancestors

    def get_descendants(self):
        """
        Retrieves the list of descendant categories for the current category.

        Uses recursion to find all child categories under the current category.

        Returns:
            list: A list of descendant Category objects.
        """
        descendants = []
        children = self.sub_categories.all()
        for child in children:
            descendants.append(child)
            descendants.extend(child.get_descendants())
        return descendants

    class Meta:
        ordering = ['name']
