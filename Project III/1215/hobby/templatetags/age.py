from datetime import datetime
from django import template


register = template.Library()

@register.filter
def age(value):
    now = datetime.today().year
    try:
        difference = now - value.replace(tzinfo=None).year
    except:
        return value
    return '%(time)s' % {'time': difference}