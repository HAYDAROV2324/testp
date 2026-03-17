from django import template

register = template.Library()

@register.filter
def lookup(dictionary, key):
    """
    Dictionary'dan value'ni olish uchun filter
    """
    if dictionary is None:
        return ''
    return dictionary.get(key, '')
