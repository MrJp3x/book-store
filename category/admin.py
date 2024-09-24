from django.contrib import admin
from .models import Category, BookType


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'book_type',
                    'category_hierarchy'
                    ]
    list_filter = ('book_type',)
    search_fields = ('name',)

    class Media:
        """
        اضافه کردن CSS سفارشی برای بهتر کردن نمایش سلسله‌مراتب.
        """
        css = {
            'all': ('css/admin_custom.css',)
        }
    # list_display = BaseCategoryAdmin.list_display + ["category_hierarchy", 'id']

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
        return queryset.order_by('book_type__id', 'id')


class BaseCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(BookType, BaseCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
