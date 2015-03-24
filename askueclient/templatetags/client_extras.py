from django import template
from askueclient.models import Point
from askueclient.models import Groups

register=template.Library()

@register.inclusion_tag('askueclient/points.html')
def get_points_list():
    point_dict={}
    pt=[]
    gp_pt=[]
    gpt={}
    groups=Groups.objects.all()
    for i in range(len(groups)):
        id_group=groups[i].id
        group=Groups.objects.get(pk=id_group)
        gr_name=group.name
        points=group.point_set.all()
        #gpt[gr_name]=points
        pt.append(group)
        for i in points:
            pt.append(i)        
        #for i in range(len(points)):
        #    nmp=points[i].name
        #    pt.append(nmp)
        gp_pt.append(pt)
        pt=[]
    point_dict['points']=gp_pt
   
    
   # points=Point.objects.all()
   # point_dict['points']=points
   # point_dict['groups']=groups
    return point_dict
