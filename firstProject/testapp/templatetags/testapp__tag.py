import datetime
from django import template

register = template.Library()

@register.simple_tag(name="Today")
def get_date():
    n=datetime.datetime.now()
    return n


def quotes(value):
    s=""+str(value)+""
    return s