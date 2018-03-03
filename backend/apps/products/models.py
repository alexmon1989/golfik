from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from backend.abstract_models import SeoModel, TimeStampedModel


class CategoryManager(models.Manager):
    def enabled(self):
        """Возвращает категории с is_enabled=True."""
        return super(CategoryManager, self).get_queryset().filter(is_enabled=True)


class Category(SeoModel, TimeStampedModel):
    """Модель категории товаров."""
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField(
        'Slug',
        max_length=255,
        unique=True,
        help_text='Используется при формировании ссылки на страницу категории.'
    )
    image = models.ImageField(
        'Изображение',
        upload_to='categories/',
        blank=True,
        null=True,
        help_text='Оптимальное разрешение - 400px * 270px'
    )
    text = RichTextUploadingField('Текст', blank=True, null=True)
    weight = models.PositiveIntegerField(
        'Вес',
        help_text='Чем больше вес, тем "выше" категория отображается на странице.',
        default=1
    )
    is_enabled = models.BooleanField('Включено', default=True)

    objects = CategoryManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products_list', args=[self.slug])

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


class ProductManager(models.Manager):
    def enabled(self):
        """Возвращает товары с is_enabled=True."""
        return super(ProductManager, self).get_queryset().filter(
            is_enabled=True,
            category__isnull=False,
            category__is_enabled=True
        )


class Product(SeoModel, TimeStampedModel):
    """Модель товара."""
    CURRENCIES = (
        (1, 'Гривна'),
        (2, 'Доллар'),
    )

    title = models.CharField('Название', max_length=255)
    slug = models.SlugField(
        'Slug',
        max_length=255,
        help_text='Используется при формировании ссылки на страницу товара.'
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', null=True, blank=True)
    text = RichTextUploadingField('Текст', blank=True, null=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, verbose_name='Подходит для', blank=True, null=True)
    price = models.PositiveIntegerField('Стоимость', blank=True, null=True)
    currency = models.PositiveSmallIntegerField(
        'Валюта',
        choices=CURRENCIES,
        default=1
    )
    in_stock = models.BooleanField('В наличии', default=True)
    is_enabled = models.BooleanField('Включено', default=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_first_photo(self):
        """Возвращает первую фотографию продукта или None, если изображений нету."""
        image = self.productphoto_set.filter(is_visible=True).order_by('created_at').first()
        if not image:
            return None
        return image

    def get_photos(self):
        """Возвращает все видимые фотографии продукта."""
        return self.productphoto_set.filter(is_visible=True).order_by('created_at')

    def get_absolute_url(self):
        if self.category:
            return reverse('product_detail', args=[self.category.slug, self.pk, self.slug])
        return '/'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('-created_at',)
        permissions = (("can_see_price", "Может смотреть цену"),)


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
        ordering = ('created_at',)
