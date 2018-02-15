from django.db import models
from backend.abstract_models import SeoModel, TimeStampedModel


class Contact(SeoModel, TimeStampedModel):
    """Модель страницы Контакты."""
    phone = models.CharField('Телефон', max_length=255)
    email = models.EmailField('E-Mail')
    form_email = models.EmailField(
        'E-Mail формы контактов',
        help_text='На этот E-Mail будут отправляться данные формы контактов при её отправке.'
    )

    def __str__(self):
        return 'Страница "Контакты"'

    class Meta:
        verbose_name = 'Данные страницы'
        verbose_name_plural = 'Данные страницы'
