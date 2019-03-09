# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import time
import copy
import urllib2
import urllib
from django.http import HttpResponse
from django.shortcuts import render
from oriented import views as or_view
from common import config
from common.gm_redis import BackUpDao
import logging

logger = logging.getLogger('GM')


def get_use_dict(type):
    show_all = or_view.get_all_oriented(type)
    educe_game_dict = {}
    for i in show_all:
        i.name = config.OWN_WXAPPID_CONFIG.get(i.name, '')
        educe_game = ''
        func = or_view.ORIENTED_TYPE_GET_EDUCENAME_FUNC.get(type)
        if func:
            educe_game = func(i.id)
        educe_game_dict[i.id] = educe_game if educe_game else '_'

    content = {
        'data': show_all,
        'educe': educe_game_dict,
        'type': '推送管理--' + or_view.ORIENTED_TYPE.get(type, ''),
        'typeId': int(type) if type else 200,
        'gameChoice': config.OWN_WXAPPID_CONFIG
    }

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
        look_all, _ = func(basic_id)

    return HttpResponse(json.dumps(look_all, indent=4, ensure_ascii=False, separators=(',', ':')),
                        content_type="application/json,charset=utf-8")


def push_fz(request, basic_id, type_id, version_id):
    return push_data(request, basic_id, type_id, version_id)


def push_online(request, basic_id, type_id, version_id):
    return push_data(request, basic_id, type_id, version_id, fz=False)


def push_data(request, basic_id, type_id, version_id, fz=True):
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

            get_all_data, wxAppIdList = func(basic_id)
            socket_url = socketList[0] if fz else socketList[1]

            api_url = socket_url + config.gain_SetSocketApi(obj[0].socket_url)
            values = {
                'versionId': version_id,
                'typeId': or_view.ORIENTED_TYPE_SERVER_ID[type_id],
                'gameId': obj[0].game_id,
                'oriented': get_all_data
            }
            # 进行参数封装
            data = urllib.urlencode(values)
            # 组装完整url
            req = urllib2.Request(api_url, data)
            # 访问完整url
            response = urllib2.urlopen(req)

            html = eval(response.read())
            if html.get('code') == 0:
                values.pop('oriented')
                test_url = socket_url + config.gain_GetSocketApi(obj[0].socket_url) + "?" + urllib.urlencode(values)

                info = {
                    'info': '成功',
                    'url': test_url,
                    'navigateToMiniProgramAppIdList': wxAppIdList,
                    'educeGameName':[config.WXAPPID_CONFIG.get(i, '') for i in wxAppIdList]
                }
                # 保存redis数据
                # save_push_data_in_redis(gameId, fz, type_id, get_all_data)
                # BackUpDao.saveGameId(gameId, gameName)
            else:
                info = {'info': '失败', 'code': html.get('code')}
        else:
            raise 'socketList is error %s %s %s' % (basic_id, type_id, fz)
    except Exception, e:
        info = {'info': '失败! %s' % e}

    logger.info('gameId={} name={} type={} fz={} data={}'.format(gameId, gameName, type, fz, json.dumps(info)))

    return HttpResponse(json.dumps(info, indent=4, ensure_ascii=False, separators=(',', ':')),
                        content_type="application/json,charset=utf-8")


def look_fz(request, basic_id, type_id, version_id):
    return look_data(request, basic_id, type_id, version_id)


def look_online(request, basic_id, type_id, version_id):
    return look_data(request, basic_id, type_id, version_id, fz=False)


def look_data(request, basic_id, type_id, version_id, fz=True):
    obj = or_view.get_curr_oriented(basic_id, type_id)
    socketList = config.getSocketUrl(obj[0].socket_url)

    gameId = obj[0].game_id
    gameName = obj[0].name
    type = or_view.ORIENTED_TYPE.get(type_id)

    try:
        if socketList:
            socket_url = socketList[0] if fz else socketList[1]

            api_url = socket_url + config.gain_GetSocketApi(obj[0].socket_url)
            values = {
                'typeId': or_view.ORIENTED_TYPE_SERVER_ID[type_id],
                'gameId': obj[0].game_id,
                'versionId': version_id
            }

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

    return HttpResponse(json.dumps(info, indent=4, ensure_ascii=False, separators=(',', ':')),
                        content_type="application/json,charset=utf-8")



# 游戏选择
def search_game(request, type_id):
    game_wxAppId = request.GET.get('search_wxAppId')
    game_wxAppId_datas = or_view.get_wxAppId_oriented(type_id, game_wxAppId)

    educe_game_dict = {}
    for i in game_wxAppId_datas:
        i.name = config.OWN_WXAPPID_CONFIG.get(i.name, '')
        educe_game = ''
        func = or_view.ORIENTED_TYPE_GET_EDUCENAME_FUNC.get(type_id)
        if func:
            educe_game = func(i.id)
        educe_game_dict[i.id] = educe_game if educe_game else '_'

    content = {
        'wxAppIdData': game_wxAppId_datas,
        'educe': educe_game_dict,
        'type': '推送管理--' + or_view.ORIENTED_TYPE.get(type_id, ''),
        'typeId': type_id,
        'gameChoice': config.OWN_WXAPPID_CONFIG
    }

    return render(request, 'push/data.html', content)

# 备份管理
def save_push_data_in_redis(gameId, fz, typeId, value):
    game_datas = BackUpDao.getData(gameId, typeId, fz)
    if len(game_datas) == 3:
        game_datas.pop(0)
    timestamp = int(time.time())

    game_datas.append([timestamp, gameId, value])

    BackUpDao.saveData(gameId, game_datas, typeId, fz)


def get_push_data_in_redis(gameId, fz, typeId):
    game_datas = BackUpDao.getData(gameId, typeId, fz)
    return game_datas


def get_all_push_data_in_redis(fz, typeId):
    game_datas = BackUpDao.getAllDatas(typeId, fz)
    return game_datas


def get_all_back_data(request):
    type = request.GET.get('type', None)
    content = {
        'type': '备份管理--' + or_view.ORIENTED_TYPE.get(type, ''),
        'typeId': type,
    }
    return render(request, 'push/backup.html', content)


def get_backup_data(request, type_id):
    env_id = request.GET.get('env_id')

    temp_data = get_all_push_data_in_redis(env_id, type_id)

    response = []
    for gameId, _temp in temp_data.items():
        push_data = eval(copy.deepcopy(_temp))
        push_data.reverse()

        for _data in push_data:
            res = {}
            res['name'] = BackUpDao.getGameId(_data[1])
            res['time'] = config.timeStampToStr(_data[0])
            res['educe'] = or_view.backup_educe_name(type_id, _data[2])

            response.append(res)

    content = {
        'type': '备份管理--' + or_view.ORIENTED_TYPE.get(type_id, ''),
        'typeId': type_id,
        'data': response,
        'socket_url': env_id
    }

    return render(request, 'push/backup.html', content)