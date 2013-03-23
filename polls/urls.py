from django.conf.urls import patterns, url
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from polls import views
from polls.models import Poll

urlpatterns = patterns('',
    # ex: /polls/
    # url(r'^$', views.index, name='index'),
    url(r'^$', ListView.as_view(
    						queryset = Poll.objects.all().order_by('-pub_date')[:5],
    						template_name = "index.html")),
    # ex: /polls/5/
    # url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(
    						model = Poll,
    						template_name = "detail.html")),
    # ex: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)