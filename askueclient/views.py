from django.shortcuts import render, render_to_response 
from django.http import HttpResponse, HttpResponseRedirect 
from django.template import loader
import datetime
from datetime import datetime
from datetime import date
import json
from json import JSONEncoder


# Create your views here.

from askueclient.models import Data30M
from askueclient.models import Data1H
from askueclient.models import TimeDay
from askueclient.models import Point
from askueclient.forms  import NameForm
def like_category(request, point_id):

    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['point_id']
    likes = 0
    if cat_id:
        cat =Point.objects.get(id=cat_id)
        catid=[cat.name]
    return HttpResponse(catid)
    
def index(request):
    zn_list=Data30M.objects.order_by('-point')[:5]
    context_dict={'categories': zn_list}
    return render(request, 'askueclient/index.html', context_dict)
    
def calendar(request):
    zn_list=Data30M.objects.order_by('-point')[:5]
    context_dict={'categories': zn_list}
    return render(request, 'askueclient/cal.html', context_dict)

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
    try:
        pk=request.POST['date1']
        pd=request.POST['date2']
    except (KeyError, 'name DoesNotExist'):
        # Redisplay the question voting form.
        return render(request, 'askueclient/about.html', {
            'error_message': "You didn't select a choice.",
        })
    else:
        context_dict={'pk':pk}
        context_dict.update({'pd': pd})
        #return HttpResponse(context_dict)
        return render(request, 'askueclient/about.html', context_dict)
    #return HttpResponse( "Rango saya hello!")
    
   # response="You're looking at the results of point %s."
   # return HttpResponse(response % point)
def name(request):
    context_dict={}
    return render(request, 'askueclient/name.html', context_dict)
    
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
        zs=zn.number_30min
        fdict.append(zs)
    return fdict

def results(request, point_id):
#    template=loader.get_template('askueclient/result1.html')
#    response = "You're looking at the results of point  %s."
#    context={'say' : response }
#    return render(request, 'askueclient/result1.html', context )
    if request.method == 'GET':
        from datetime import date
        flistres=[]
        number=[]
        num=0
        context_dict={}
        current_date=date.today()
        str_date=current_date.strftime('%d.%m.%Y')
    #ftime=TimeDay.objects.get(id=1)
        fftime=ftime()
        zn_list=Data30M.objects.order_by('-zn')[:5]
        for i in [1,2,3,4]:
            result=query(Data30M, point_id,i)
            for n in range(len(result)):
                flistres.append(result[n].zn)
            context_dict['zn'+str(i)]=flistres
            flistres=[]
        for i in range(len(context_dict['zn1'])):
            number.append(i)
        point_number=que_point(point_id)
        context_dict.update({'number': number})
        context_dict.update({'categories': zn_list})
        context_dict.update({'str_date': str_date})
        context_dict.update({'ftime': fftime})
        context_dict.update({'results':result})
        context_dict.update({'point_n':point_number})
        return render(request, 'askueclient/result1.html', context_dict)
    if request.method == 'POST':
        try:
            pk=request.POST['date1']
            pd=request.POST['date2']
            point_number=que_point(point_id)
        except (KeyError, 'name DoesNotExist'):
            # Redisplay the question voting form.
            return render(request, 'askueclient/about.html', {
             'error_message': "You didn't select a choice.",
            })
        else:
            context_dict={'pk':pk}
            context_dict.update({'pd': pd})
            context_dict.update({'point_n':point_number})
            #return HttpResponse(context_dict)
            return render(request, 'askueclient/result1.html', context_dict)

def query(table,point_id, pr):
	queue= table.objects.filter(point=point_id).filter(dtime__gte=date.today()).filter(param=pr).order_by('dtime')
	return queue
	

	
def que_point(point_id):
    queue= Point.objects.filter(id=point_id)
    return queue
    
def time_30(request, point_id):
    current_date=date.today()
    str_date=current_date.strftime('%d.%m.%Y')
    pn_id = None
    flistres=[]
    fdict={}
    flist=[]
    if request.method == 'GET':
        pn_id = request.GET['point_id']
    for i in [1,2,3,4]:
        result=query(Data30M, pn_id, i)
        for n in range(len(result)):
            flistres.append(result[n].zn)
        fdict['zn'+str(i)]=flistres
        flistres=[]
    for i in range(1,49):
        zn=TimeDay.objects.get(id=i)
        zs=zn.number_30min
        flist.append(zs)
    fdict['ftime']=flist
    fdict['cur_day']=str_date
    #fdict['zn']=flistres
    data=json.dumps(fdict)
    data = JSONEncoder().encode(fdict)
    return HttpResponse(data)
    
def time_hour(request, point_id):
    current_date=date.today()
    str_date=current_date.strftime('%d.%m.%Y')
    pn_id = None
    flistres=[]
    fdict={}
    flist=[]
    if request.method == 'GET':
        pn_id = request.GET['point_id']
    for i in [1,2,3,4]:
        result=query(Data1H, pn_id, i)
        for n in range(len(result)):
            flistres.append(result[n].zn)
        fdict['zn'+str(i)]=flistres
        flistres=[]
    for i in range(1,25):
        zn=TimeDay.objects.get(id=i)
        zs=zn.number_1hour
        flist.append(zs)
    fdict['ftime']=flist
    fdict['cur_day']=str_date
    #fdict['zn']=flistres
    data=json.dumps(fdict)
    data = JSONEncoder().encode(fdict)
    return HttpResponse(data)
       
    
    
#def get_name(request):
#    try:
#        pk=request.POST['your_name']
#    except (KeyError, 'name DoesNotExist'):
#        # Redisplay the question voting form.
#        return render(request, 'askueclient/name.html', {
#            'error_message': "You didn't select a choice.",
#        })
#    else:
#        context_dict={'pk':pk}
#        #return HttpResponse(context_dict)
#        return render(request, 'askueclient/about.html', context_dict)
        

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'askueclient/name.html', {'form': form})
