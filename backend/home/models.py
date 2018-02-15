from django.db import models
from backend.abstract_models import SeoModel, TimeStampedModel
from ckeditor.fields import RichTextField


class Home(SeoModel, TimeStampedModel):
    """Модель страницы Главная."""
    meta_h1 = models.CharField('Текст 1', max_length=255, blank=False)
    text_2 = models.CharField('Текст 2', max_length=255, blank=False)
    text_3 = RichTextField('Текст 3', blank=False)

    def __str__(self):
        return 'Главная страница'

    class Meta:
        verbose_name = 'Данные страницы'
        verbose_name_plural = 'Данные страницы'
