from django.conf.urls import include, patterns, url
from about.views import first

urlpatterns = patterns('', url(r'^$', first, name='about'))