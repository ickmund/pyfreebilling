from django import template
from django.conf import settings

#from easy_thumbnails.files import get_thumbnailer

#from pyfreebill.models import PyfbSettings

register = template.Library()

ALLOWABLE_VALUES = ("PYFB_CP_MENU_TYPE_INV", "PYFB_CP_LOGO_NAME", "PYFB_CP_COMPANY_NAME")

# settings value
@register.simple_tag
def settings_value(name):
    """ Usage : {% settings_value "CONSTANT_NAME_1" %} """
    is_allowable = [x for x in ALLOWABLE_VALUES if x == name]
    if len(is_allowable) > 0:
        return getattr(settings, name, '')
#    if name == "LOGO":
#        return get_thumbnailer(PyfbSettings.logo)['avatar'].url
    return ''