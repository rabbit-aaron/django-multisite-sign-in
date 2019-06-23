from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag(takes_context=True)
def other_domains(context):
    request = context['request']
    current_domain = request.META['HTTP_HOST']
    return [i for i in settings.DOMAINS if i != current_domain]
