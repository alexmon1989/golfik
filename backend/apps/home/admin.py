from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import Home


class HomeAdmin(SingleModelAdmin):
    """Класс для описание интерфейса администрирования модели Home."""
    fieldsets = (
        (None, {
            'fields': ('meta_h1', 'text_2', 'text_3', )
        }),
        ('SEO опции', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_keywords', 'meta_description'),
        }),
    )


admin.site.register(Home, HomeAdmin)
