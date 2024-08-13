from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return f'{self.name}'



    def get_ancestors(self):
        """
        Returns a list of ancestors for this category, starting from the root.
        """
        ancestors = []
        category = self
        while category.parent:
            ancestors.insert(0, category.parent)
            category = category.parent
        return ancestors

    def get_descendants(self):
        """
        Returns a list of descendants for this category.
        """
        descendants = []
        children = self.children.all()
        for child in children:
            descendants.append(child)
            descendants.extend(child.get_descendants())
        return descendants

    class Meta:
        ordering = ['name']
