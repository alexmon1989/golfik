from django.db import models
from ckeditor.fields import RichTextField
from backend.abstract_models import SeoModel, TimeStampedModel


class About(SeoModel, TimeStampedModel):
    """Модель страницы О нас."""
    title = models.CharField('Заголовок', max_length=255, blank=False)
    under_title_text = models.CharField('Текст под заголовком', max_length=255, blank=True, null=True)
    text = RichTextField('Текст', blank=False)
    image = models.ImageField(
        'Изображение',
        upload_to='about/',
        blank=True,
        null=True,
        help_text='Оптимальный размер: 1200px*750px.'
    )
    image_text = models.CharField('Подпись под изображением', max_length=255, blank=True, null=True)

    def __str__(self):
        return 'Страница "О нас"'

    class Meta:
        verbose_name = 'Данные страницы'
        verbose_name_plural = 'Данные страницы'
