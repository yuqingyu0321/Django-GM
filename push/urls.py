from django.conf.urls import include, url,static

from .views import showAll, lookJson, push_fz

urlpatterns = [
    url(r'^$', showAll),
    url(r'look/(?P<basic_id>\d+)/(?P<type_id>\d+)', lookJson),
    url(r'fz/(?P<basic_id>\d+)', push_fz),
]
