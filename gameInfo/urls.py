from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'gameInfo/list.html', GameInfoView.handleList),
    url(r'gameInfo/add.html', GameInfoView.handleAdd),
    url(r'gameInfo/save.html', GameInfoView.handleSave),
    url(r'gameInfo/look.html', GameInfoView.handleLook),
    url(r'gameInfo/update.html', GameInfoView.handleUpdate),
    url(r'gameInfo/del.html', GameInfoView.handleDel),
    url(r'gameInfo/delAll.html', GameInfoView.handleDelAll),
    url(r'gameInfo/data.html', GameInfoView.handleData),
]