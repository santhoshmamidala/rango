from django.conf.urls import patterns, url, include
from RangoApp.views import index
from about.views import first
from contact.views import info

urlpatterns = patterns('', url(r'^$', index, name='index'),
                       url(r'^about/', first, name='about'),
                       url(r'^contact/', info, name='contact'))
