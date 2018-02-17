from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from backend.abstract_models import SeoModel, TimeStampedModel


class Category(SeoModel, TimeStampedModel):
    """Модель категории товаров."""
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField(
        'Slug',
        max_length=255,
        unique=True,
        help_text='Используется при формировании ссылки на страницу категории.'
    )
    image = models.ImageField('Изображение', upload_to='categories/', blank=True, null=True)
    text = RichTextUploadingField('Текст', blank=True, null=True)
    weight = models.PositiveIntegerField(
        'Вес',
        help_text='Чем больше вес, тем "выше" категория отображается на странице.',
        default=1
    )
    is_enabled = models.BooleanField('Включено', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)


class Car(TimeStampedModel):
    """Модель автомобиля (модели)."""
    title = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Модель автомобиля'
        verbose_name_plural = 'Модели автомобилей'
        ordering = ('title',)


class Product(SeoModel, TimeStampedModel):
    """Модель товара."""
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField(
        'Slug',
        max_length=255,
        unique=True,
        help_text='Используется при формировании ссылки на страницу товара.'
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    text = RichTextUploadingField('Текст', blank=True, null=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, verbose_name='Подходит для', blank=True, null=True)
    price = models.PositiveIntegerField('Стоимость', blank=True, null=True)
    currency = models.PositiveSmallIntegerField(
        'Валюта',
        choices=(
            (1, 'Гривна'),
            (2, 'Доллар'),
        ),
        default=1
    )
    is_enabled = models.BooleanField('Включено', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('-created_at',)


class ProductPhoto(TimeStampedModel):
    """Модель фотографии товара."""

    def upload_to(instance, filename):
        return 'products/{}/{}'.format(instance.product.pk, filename)

    image = models.ImageField(
        'Изображение',
        upload_to=upload_to,
        help_text='Оптимальный размер: 800px*500px.'
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    is_visible = models.BooleanField('Включено', default=True)

    def __str__(self):
        return 'Изображение #{}'.format(self.pk)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Галерея товара'
