from django.conf.urls import patterns, url

from institutions import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    url(r'^/$', views.home, name='schools'),
    url(r'^/(?P<slug>[\w-]+)/$', views.seeschool, name='seeschool'),
    url(r'^add-school/$', views.addschool, name='addschool'),
    url(r'^/top-schools/$', views.topschools, name='topschools'),
)