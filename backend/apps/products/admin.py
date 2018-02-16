from django.contrib import admin
from .models import Car, Category, Product, ProductPhoto


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    """Класс для описание интерфейса администрирования модели Car."""
    list_display = ('title', 'updated_at', 'created_at')
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс для описание интерфейса администрирования модели Category."""
    list_display = ('title', 'weight', 'is_enabled', 'updated_at', 'created_at')
    list_filter = ('is_enabled', )
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'text', 'weight', 'is_enabled')
        }),
        ('SEO опции', {
            'classes': ('collapse',),
            'fields': ('meta_h1', 'meta_title', 'meta_keywords', 'meta_description'),
        }),
    )
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title',)
    list_editable = ('is_enabled',)


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс для описание интерфейса администрирования модели Product."""
    list_display = ('title', 'category', 'car', 'price', 'currency', 'is_enabled', 'updated_at', 'created_at')
    list_filter = ('is_enabled', 'category', 'car')
    search_fields = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'category', 'text', 'car', 'price', 'currency', 'is_enabled')
        }),
        ('SEO опции', {
            'classes': ('collapse',),
            'fields': ('meta_h1', 'meta_title', 'meta_keywords', 'meta_description'),
        }),
    )
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('is_enabled',)
    inlines = (ProductPhotoInline,)
