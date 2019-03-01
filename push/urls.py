from django.conf.urls import include, url,static

from .views import *

urlpatterns = [
    url(r'^$', showAll),
    url(r'look/(?P<basic_id>\d+)/(?P<type_id>\d+)', lookJson),
    url(r'fz/(?P<basic_id>\d+)/(?P<type_id>\d+)', push_fz),
    url(r'fzdata/(?P<basic_id>\d+)/(?P<type_id>\d+)', look_fz),
    url(r'online/(?P<basic_id>\d+)/(?P<type_id>\d+)', push_online),
    url(r'onlinedata/(?P<basic_id>\d+)/(?P<type_id>\d+)', look_online),
]
