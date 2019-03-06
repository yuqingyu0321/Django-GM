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
import logging

logger = logging.getLogger('GM')

def get_use_dict(type):
    show_all = or_view.get_all_oriented(type)
    educe_game_dict = {}
    for i in show_all:
        educe_game = ''
        func = or_view.ORIENTED_TYPE_GET_EDUCENAME_FUNC.get(type)
        if func:
            educe_game = func(i.id)
        educe_game_dict[i.id] = educe_game if educe_game else '_'

    content = {'data': show_all,
               'educe': educe_game_dict,
               'type': or_view.ORIENTED_TYPE.get(type, ''),
               'typeId': int(type) if type else 200}

    return content


def showAll(request):
    type = request.GET.get('type', None)

    if type in or_view.ORIENTED_TYPE.keys():
        return render(request, 'push/data.html', get_use_dict(type))
    else:
        return render(request, 'push/data.html')


def lookJson(request, basic_id, type_id):
    type_id = str(type_id)
    look_all = {}

    func = or_view.ORIENTED_TYPE_GET_ALL_FUNC.get(type_id)
    if func:
        look_all = func(basic_id)

    return HttpResponse(json.dumps(look_all, indent=4, ensure_ascii=False, separators=(',',':')),
                        content_type="application/json,charset=utf-8")


def push_fz(request, basic_id, type_id):
    return push_data(request, basic_id, type_id)


def push_online(request, basic_id, type_id):
    return push_data(request, basic_id, type_id, fz=False)


def push_data(request, basic_id, type_id, fz=True):
    obj = or_view.get_curr_oriented(basic_id, type_id)
    socketList = config.getSocketUrl(obj[0].socket_url)
    gameId = obj[0].game_id
    gameName = obj[0].name
    type = or_view.ORIENTED_TYPE.get(type_id)

    try:
        if socketList:
            func = or_view.ORIENTED_TYPE_GET_ALL_FUNC.get(type_id)
            if not func:
                raise 'func is error %s %s %s' % (basic_id, type_id, fz)

            get_all_data = func(basic_id)
            socket_url = socketList[0] if fz else socketList[1]

            api_url = socket_url + config.gain_SetSocketApi(obj[0].socket_url)
            values = {'typeId': or_view.ORIENTED_TYPE_SERVER_ID[type_id], 'gameId': obj[0].game_id,
                      'oriented': get_all_data}

            # 进行参数封装
            data = urllib.urlencode(values)
            # 组装完整url
            req = urllib2.Request(api_url, data)
            # 访问完整url
            response = urllib2.urlopen(req)
            html = eval(response.read())
            if html.get('code') == 0:
                info = {'info': '成功'}
            else:
                info = {'info': '失败', 'code': html.get('code')}
        else:
            raise 'socketList is error %s %s %s' % (basic_id, type_id, fz)
    except Exception, e:
        info = {'info': '失败! %s' % e}

    logger.info('gameId={} name={} type={} fz={} data={}'.format(gameId, gameName, type, fz, json.dumps(info)))

    return HttpResponse(json.dumps(info, indent=4, ensure_ascii=False, separators=(',',':')),
                        content_type="application/json,charset=utf-8")


def look_fz(request, basic_id, type_id):
    return look_data(request, basic_id, type_id)


def look_online(request, basic_id, type_id):
    return look_data(request, basic_id, type_id, fz=False)


def look_data(request, basic_id, type_id, fz=True):
    obj = or_view.get_curr_oriented(basic_id, type_id)
    socketList = config.getSocketUrl(obj[0].socket_url)

    gameId = obj[0].game_id
    gameName = obj[0].name
    type = or_view.ORIENTED_TYPE.get(type_id)

    try:
        if socketList:
            func = or_view.ORIENTED_TYPE_GET_ALL_FUNC.get(type_id)
            if not func:
                raise 'func is error %s %s %s' % (basic_id, type_id, fz)

            socket_url = socketList[0] if fz else socketList[1]

            api_url = socket_url + config.gain_GetSocketApi(obj[0].socket_url)
            values = {'typeId': or_view.ORIENTED_TYPE_SERVER_ID[type_id], 'gameId': obj[0].game_id}

            # 进行参数封装
            data = urllib.urlencode(values)
            # 组装完整url
            req = urllib2.Request(api_url, data)
            # 访问完整url
            response = urllib2.urlopen(req)
            info = eval(response.read())

        else:
            raise 'socketList is error %s %s %s' % (basic_id, type_id, fz)
    except Exception, e:
        info = {'info': '失败! %s' % e}

    logger.info('gameId={} name={} type={} fz={} data={}'.format(gameId, gameName, type, fz, json.dumps(info)))

    return HttpResponse(json.dumps(info, indent=4, ensure_ascii=False, separators=(',',':')),
                        content_type="application/json,charset=utf-8")
