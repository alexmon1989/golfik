# Generated by Django 2.0.2 on 2018-02-15 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='text_3',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='text_1',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='text_2',
            new_name='under_title_text',
        ),
    ]
