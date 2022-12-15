from datetime import datetime, timedelta
from django import template
from django.utils.timesince import timesince

register = template.Library()

@register.filter
def extra_timesince(value):
    now = datetime.now()
    try:
        difference = now - value.replace(tzinfo=None)
    except:
        return value

    if difference <= timedelta(minutes=1):
        return 'just now'
    return '%(time)s 전' % {'time': timesince(value).split(', ')[0]}