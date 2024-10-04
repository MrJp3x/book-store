from django.contrib import admin
from .models import PhysicalBook, EBook, AudioBook, ProductType


class BaseCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(ProductType, BaseCategoryAdmin)


@admin.register(PhysicalBook)
class PhysicalBookAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'dimensions', 'cover_type', 'number_of_pages')
    search_fields = ('name',)

@admin.register(EBook)
class EBookAdmin(admin.ModelAdmin):
    list_display = ('name', 'file_format', 'file_size', 'number_of_pages')
    search_fields = ('name',)

@admin.register(AudioBook)
class AudioBookAdmin(admin.ModelAdmin):
    list_display = ('name', 'audio_length', 'narrator', 'episode_count')
    search_fields = ('name', 'narrator')