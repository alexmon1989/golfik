# Generated by Django 2.0.2 on 2018-02-15 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_h1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тег h1 (мета-тег)')),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title (мета-тег)')),
                ('meta_keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name='Keywords (мета-тег)')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Description (мета-тег)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='E-Mail')),
                ('form_email', models.EmailField(help_text='На этот E-Mail будут отправляться данные формы контактов при её отправке.', max_length=254, verbose_name='E-Mail формы контактов')),
            ],
            options={
                'verbose_name': 'Данные страницы',
                'verbose_name_plural': 'Данные страницы',
            },
        ),
    ]