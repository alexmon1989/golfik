from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import About


class AboutAdmin(SingleModelAdmin):
    """Класс для описание интерфейса администрирования модели About."""
    fieldsets = (
        (None, {
            'fields': ('title', 'under_title_text', 'text', 'image', 'image_text')
        }),
        ('SEO опции', {
            'classes': ('collapse',),
            'fields': ('meta_h1', 'meta_title', 'meta_keywords', 'meta_description'),
        }),
    )


admin.site.register(About, AboutAdmin)
