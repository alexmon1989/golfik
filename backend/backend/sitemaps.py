from django.contrib import sitemaps
from django.urls import reverse
from apps.products.models import Category, Product


class StaticViewSitemap(sitemaps.Sitemap):
    """Карта сайта для стат. страниц."""
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'about', 'contacts', 'delivery']

    def location(self, item):
        return reverse(item)


class CategorySitemap(sitemaps.Sitemap):
    """Карта сайта для категорий."""
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Category.objects.enabled()

    def lastmod(self, obj):
        return obj.updated_at


class ProductSitemap(sitemaps.Sitemap):
    """Карта сайта для товаров."""
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return Product.objects.enabled()

    def lastmod(self, obj):
        return obj.updated_at
