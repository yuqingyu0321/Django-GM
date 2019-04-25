from django.conf.urls import url

from .views import UpView

urlpatterns = [
    url(r'upload/up/list.html', UpView.handleList),
    url(r'upload/up/data.html', UpView.handleData),
    url(r'upload/up/add.html', UpView.handleAdd),
    url(r'upload/up/save.html', UpView.handleSave),
    url(r'upload/up/del.html', UpView.handleDel),
    url(r'upload/up/delAll.html', UpView.handleDelAll),
    url(r'upload/up/lookInfo.html', UpView.handleLookInfo),
    url(r'upload/up/look.html', UpView.handleLook),
    url(r'upload/up/update.html', UpView.handleUpdate),

    url(r'upload/load/list.html', UpView.handleLoadList),
    url(r'upload/load/data.html', UpView.handleLoadData),
    url(r'upload/load/load.html', UpView.handleLoad),
]