from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'lecturers.views.home', name='home'),
    url(r'^lecturers/$', 'lecturers.views.lecturer', name='lecturers'),
    url(r'^add-lecturer/$', 'lecturers.views.addlecturer', name='addlecturers'),
    url(r'^contact-us', 'lecturers.views.contactus', name='contactus'),
    url(r'^about-us', 'lecturers.views.aboutus', name='aboutus'),
    url(r'^help', 'lecturers.views.help', name='help'),
    url(r'^schools/$', 'institutions.views.home', name='schools'),
    url(r'^add-school/$', 'institutions.views.addschool', name='addschool'),
    url(r'^top-schools', 'institutions.views.topschools', name='top-schools'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)