import os
import shutil
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Product


@receiver(post_delete, sender=Product)
def delete_directory(sender, instance, **kwargs):
    """Обработчик сигнала удаления продукта.
    Выполняет удаление каталога с изображениями продукта."""
    path = os.path.join(settings.MEDIA_ROOT, 'products', str(instance.pk))
    shutil.rmtree(path)
