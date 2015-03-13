from django import template
from askueclient.models import Point

register=template.Library()

@register.inclusion_tag('askueclient/points.html')
def get_points_list():
    return {'points': Point.objects.all()}
