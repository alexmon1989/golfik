from django import template
from apps.products.models import Category
from apps.contacts.models import ContactTemplate

register = template.Library()


@register.filter
def in_list(value, the_list):
    value = str(value)
    return value in the_list.split(',')


@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()


@register.simple_tag
def categories():
    return Category.objects.enabled().order_by('-weight')


@register.simple_tag
def contacts():
    return ContactTemplate.objects.filter(is_enabled=True).order_by('contact_type')
