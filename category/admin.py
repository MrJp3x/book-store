from django.contrib import admin
from .models import Category, GeneralCategory


@admin.register(GeneralCategory)
class GeneralCategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name',]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'sub_parent', 'category_hierarchy']
    search_fields = ['name']

    def category_hierarchy(self, obj):
        ancestors = obj.get_ancestors()
        if ancestors:
            return ' > '.join([ancestor.name for ancestor in ancestors] + [obj.name])
        return obj.name

    category_hierarchy.short_description = "Category Hierarchy"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sub_parent":
            kwargs["queryset"] = Category.objects.filter(sub_parent__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
