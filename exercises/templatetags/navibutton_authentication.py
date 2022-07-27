from django.utils.safestring import mark_safe
from django import template
register = template.Library()

@register.simple_tag
def navibutton_authentication(data):
  if data == True:
    return "Change password" 
  else:
    # return "register" , "login"
    return mark_safe("<a href="">register</a>, <a href="">login</a>") 
    # return mark_safe("<a href="">Register</a>")