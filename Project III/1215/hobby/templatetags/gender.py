from django import template

register = template.Library()

@register.filter
def gender(value):
    if value == 'M':
        gender = '♂'
    else:
        gender = '♀'
    return gender