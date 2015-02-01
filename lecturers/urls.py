from django.conf.urls import patterns, url

from lecturers import views

urlpatterns = patterns('',
   
    #url(r'^$', views.index, name='index'),
    url(r'^/$', views.lecturer, name='lecturer'),
    url(r'^/(?P<slug>[\w-]+)/$', views.seelecturer, name='seelecturer'),
    url(r'^add-lecturer/$', views.addlecturer, name='addlecturers'),
)