from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = 'apps.products'
    verbose_name = 'Товары'

    def ready(self):
        import apps.products.signals
