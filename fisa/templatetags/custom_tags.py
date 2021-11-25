from django import template
import re

register = template.Library()

numeric_test = re.compile("^\d+$")
register = template.Library()

def getattribute(value, arg):
    """Gets an attribute of an object dynamically from a string name"""
    print(getattr(value, arg))
    return getattr(value, arg)

@register.filter(name='get_form_field')
def get_form_field(adminform, field_name):
    try:
        return adminform[field_name]
    except KeyError:
        return "invalid"

register.filter('getattribute', getattribute)