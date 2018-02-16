from ckeditor_uploader.fields import RichTextUploadingField
from backend.abstract_models import SeoModel, TimeStampedModel


class Contact(SeoModel, TimeStampedModel):
    """Модель страницы Контакты."""
    text = RichTextUploadingField('Текст', blank=False)

    def __str__(self):
        return 'Страница "Контакты"'

    class Meta:
        verbose_name = 'Данные страницы'
        verbose_name_plural = 'Данные страницы'
