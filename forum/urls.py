from django.conf.urls import patterns, url

from forum import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^state/(\d+)/$', views.state, name='state'),
    #url(r'^(\d+)/$', views.pawan, name='pawan')

)