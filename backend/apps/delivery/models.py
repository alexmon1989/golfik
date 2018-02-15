from ckeditor_uploader.fields import RichTextUploadingField
from backend.abstract_models import SeoModel, TimeStampedModel


class Delivery(SeoModel, TimeStampedModel):
    """Модель страницы Оплата, доставка."""
    text = RichTextUploadingField('Текст', blank=False)

    def __str__(self):
        return 'Страница "Оплата, доставка"'

    class Meta:
        verbose_name = 'Данные страницы'
        verbose_name_plural = 'Данные страницы'
