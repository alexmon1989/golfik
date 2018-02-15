from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import Delivery


class DeliveryAdmin(SingleModelAdmin):
    """Класс для описание интерфейса администрирования модели Delivery."""
    fields = (
        'text',
        'meta_h1',
        'meta_title',
        'meta_keywords',
        'meta_description'
    )


admin.site.register(Delivery, DeliveryAdmin)
