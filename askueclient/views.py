from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.

from askueclient.models import Data30M
from askueclient.models import TimeDay

def index(request):
    zn_list=Data30M.objects.order_by('-point')[:5]
    context_dict={'categories': zn_list}
    return render(request, 'askueclient/index.html', context_dict)

def detail(request):
    from datetime import date
    current_date=date.today()
    str_date=current_date.strftime('%d.%m.%Y')
    #ftime=TimeDay.objects.get(id=1)
    fftime=ftime()
    zn_list=Data30M.objects.order_by('-zn')[:5]
    context_dict={'categories': zn_list}
    context_dict.update({'str_date': str_date})
    context_dict.update({'ftime': fftime})
    return render(request, 'askueclient/detail.html', context_dict)
   # return HttpResponse(" It's a detail page")
def about(request):
    return HttpResponse( "Rango saya hello!")
   # response="You're looking at the results of point %s."
   # return HttpResponse(response % point)

def get_cur_date(request, *args, **kwargs):
    from datetime import date
    current_date=date.today
    str_date=current_date.strftime('%d.%m.%Y')
    return render(request, 'askueclient/detail.html', {'str_date': str_date}) 
    
    
def ftime():
    fdict=[]
    name='ftime_'
    for i in range(1,50):
        zn=TimeDay.objects.get(id=i)
        zs=zn.number_5min
        fdict.append(zs)
    return fdict
