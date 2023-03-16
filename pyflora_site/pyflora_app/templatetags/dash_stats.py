""" from django import template
from django.http import HttpResponse
from pyflora_app.models import Stats

register = template.Library()

@register.simple_tag(takes_context=True)
def stats_result(context):
    pot = context
    stats_data = Stats.objects.filter(pot_senzors_id=pot).latest('stats_time')
    data = {
    'stats_data': stats_data,
    }
    return HttpResponse(data) """