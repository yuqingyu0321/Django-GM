# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import urllib2
import urllib
from django.http import HttpResponse
from django.shortcuts import render
from oriented import views as or_view
from common import config
from django.views.generic import View



def get_use_dict(type):
    show_all = or_view.get_all_oriented(type)
    educe_game_dict = {}
    for i in show_all:
        educe_game = ''
        if type == '0':
            educe_game = or_view.get_iconswitch_name(i.id)
        elif type == '1':
            educe_game = or_view.get_strip_educe_name(i.id)
        elif type == '2':
            educe_game = or_view.get_slideover_educe_name(i.id)
        educe_game_dict[i.id] = educe_game if educe_game else '_'

    content = {'data': show_all,
               'educe': educe_game_dict,
               'type': or_view.ORIENTED_TYPE.get(type, ''),
               'typeId': int(type) if type else 200}
    return content

def showAll(request):
    type = request.GET.get('type', None)
    print type
    if request.GET.get('type') == '0':
        print request.GET
    elif request.GET.get('type') == '1':
        print request.GET
    elif request.GET.get('type') == '2':
        print request.GET
    else:
        return render(request, 'push/test.html')

    return render(request, 'push/test.html', get_use_dict(type))



def lookJson(request, basic_id, type_id):
    type_id = str(type_id)
    look_all = {}
    if type_id == '0':
        look_all = or_view.get_all_iconswitch_data(basic_id)
    elif type_id == '1':
        look_all = or_view.get_all_gameStrip_data(basic_id)
    elif type_id == '2':
        look_all = or_view.get_all_SlideOver_data(basic_id)

    return HttpResponse(json.dumps(look_all),
                        content_type="application/json,charset=utf-8")


def push_fz(request, basic_id):
    content = get_use_dict()
    obj = or_view.get_curr_strip(basic_id)
    socketList = config.getSocketUrl(obj[0].socket_url)
    try:
        if socketList:
            get_all_data = or_view.get_curr_strip(basic_id)

            api_url = socketList[0] + 'api/wx/zmgm/set'
            values = {'gameId': obj[0].game_id, 'oriented': get_all_data}

            # 进行参数封装
            data = urllib.urlencode(values)
            # 组装完整url
            req = urllib2.Request(api_url, data)
            # 访问完整url
            response = urllib2.urlopen(req)
            html = response.read()

            config.flash(request, "success", "成功！")
        else:
            raise 'socketList%s' % socketList
    except:
        config.flash(request, "false", "失败！")

    return render(request, 'push/all.html', content)
