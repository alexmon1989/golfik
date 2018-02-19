from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import Contact, ContactTemplate


class ContactsAdmin(SingleModelAdmin):
    """Класс для описание интерфейса администрирования модели Contact."""
    fields = (
        'text',
        'meta_h1',
        'meta_title',
        'meta_keywords',
        'meta_description'
    )


admin.site.register(Contact, ContactsAdmin)
admin.site.register(ContactTemplate, admin.ModelAdmin)
