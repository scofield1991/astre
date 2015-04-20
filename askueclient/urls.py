from django.conf.urls import patterns, url
from askueclient import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
	    url(r'^detail/$', views.detail, name='detail'),
	    url(r'^detail/calendar$', views.calendar, name='calendar'),
        url(r'^about/$', views.about, name='about'),
        url(r'^name/$', views.get_name, name='get_name'),
      #  url(r'^(?P<point_id>\d+)/$', views.results, name='results'),
        url(r'^detail/(?P<point_id>[\w\-]+)/$', views.results, name='results'),
        url(r'^detail/(?P<point_id>[\w\-]+)/like_category/$', views.like_category, name='like_category'),
        url(r'^detail/(?P<point_id>[\w\-]+)/time_hour/$', views.time_hour, name='time_hour'),
        url(r'^detail/(?P<point_id>[\w\-]+)/time_30/$', views.time_30, name='time_30'),
        url(r'^detail/(?P<point_id>[\w\-]+)/sev_days/$', views.several_days, name='several_days')
)
