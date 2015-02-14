from django.conf.urls import patterns, url

from rates import views

urlpatterns = patterns('',
#    url(r'^$', views.index, name='index'),
    url(r'^$', views.rating, name='allRatings'),
    url(r'^/(?P<slug>[\w-]+)/$', views.ratelecturer, name='ratelecturer'),
    url(r'^/(?P<slug>[\w-]+)/add$', views.addRating, name='addRating'),
    #url(r'^/(?P<id>[\w-]+)/get_help/$', views.get_help, name='get_help'),
)