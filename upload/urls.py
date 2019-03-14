from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', show_upload),
    url(r'search/', show_game_upload),
    url(r'load/(?P<upload_id>\d+)', upload_load),
]