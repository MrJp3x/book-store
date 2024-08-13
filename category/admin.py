from django.contrib import admin
from .models import Category


class BaseCategoryAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'parent',
                    ]
    list_filter = ('parent',)
    search_fields = ('name',)

    class Media:
        """
        اضافه کردن CSS سفارشی برای بهتر کردن نمایش سلسله‌مراتب.
        """
        css = {
            'all': ('css/admin_custom.css',)
        }


class CategoryAdmin(BaseCategoryAdmin):
    list_display = BaseCategoryAdmin.list_display + ["category_hierarchy", 'id']

    def category_hierarchy(self, obj):
        """
        نمایش سلسله‌مراتبی کتگوری‌ها.
        """
        ancestors = obj.get_ancestors()
        if ancestors:
            return ' > '.join([ancestor.name for ancestor in ancestors] + [obj.name])
        return obj.name

    category_hierarchy.short_description = "Category Hierarchy"

    def get_queryset(self, request):
        """
        کوئری‌ست‌های پنل ادمین را سفارشی ‌سازی می‌کنیم تا کتگوری‌ها بر اساس سلسله‌مراتب مرتب شوند.
        """
        queryset = super().get_queryset(request)
        return queryset.order_by('parent__id', 'id')


admin.site.register(Category, CategoryAdmin)
