from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^s/$', 'lecturers.views.search', name='search'),
    url(r'^$', 'lecturers.views.home', name='home'),
    url(r'^contact-us', 'lecturers.views.contactus', name='contactus'),
    url(r'^about-us', 'lecturers.views.aboutus', name='aboutus'),
    url(r'^help','lecturers.views.help', name='help'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^lecturers', include('lecturers.urls', namespace="lecturers")),
    url(r'^institutions', include('institutions.urls', namespace="institutions")),
    url(r'^rates', include('rates.urls', namespace="rates")),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)