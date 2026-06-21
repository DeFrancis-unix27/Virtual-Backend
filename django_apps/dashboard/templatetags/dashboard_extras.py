from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def field_value(obj, attr):
    return getattr(obj, attr, "")
