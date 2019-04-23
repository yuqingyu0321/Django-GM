# -*- coding: utf-8 -*-
import json
import time
import copy
import urllib2
import urllib
from custom.view.view import ViewHelper
from django.shortcuts import render
from common import config
from django.http import HttpResponse
from gameInfo import game
from datetime import datetime
from oriented.views import (
    ORIENTED_TYPE_MODEL,
    ORIENTED_TYPE_GET_EDUCENAME_FUNC,
    ORIENTED_TYPE_GET_ALL_FUNC,
    get_curr_oriented,
    ORIENTED_TYPE_SERVER_ID,
)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def handle_userAndTime(basicId, typeId):
    currOrientedQuery = ORIENTED_TYPE_MODEL[typeId].objects.get(id=int(basicId))
    currOrientedQuery.online_modifi_time = datetime.now()
    currOrientedQuery.save(update_fields=['online_modifi_time'])

class PushView(ViewHelper):
    @classmethod
    def handleData(cls, request):
        appid = request.GET['appid'].encode("utf-8")
        type = request.GET['type'].encode("utf-8")
        if len(appid) == 18:
            pass
        else:
            config.flash(request, "提示", "请先选择游戏或检查当前游戏wxAppId正确性")
            return render(request, 'message.html')

        page = request.GET['page'].encode("utf-8")
        limit = request.GET['limit'].encode("utf-8")
        resData = []
        allData =  ORIENTED_TYPE_MODEL[type].objects.filter(name=appid).order_by('-id')

        for _temp in allData:

            educeGame = []
            func = ORIENTED_TYPE_GET_EDUCENAME_FUNC.get(type)
            if func:
                educeGame = func(_temp.id)

            _node = {
                'id': _temp.id,
                'name': game.innerGame.get(_temp.name, ''),
                'educeGame': educeGame,
                'educeGameCount': len(educeGame),
                'time': _temp.online_modifi_time.strftime('%Y-%m-%d %H:%M:%S.%f') if  _temp.online_modifi_time else ''
            }
            resData.append(_node)

        startIndex = (int(page) - 1) * int(limit)
        if startIndex + int(limit) - 1 < len(resData):
            endIndex = startIndex + int(limit)
            splitResData = resData[startIndex: endIndex]
        else:
            splitResData = resData[startIndex:]

        res = {
            'code': 0,
            'count': len(resData),
            'msg': "",
            'data': splitResData
        }
        return HttpResponse(json.dumps(res, ensure_ascii=False, separators=(',', ':')),
                            content_type="application/json,charset=utf-8")

    @classmethod
    def handleList(cls, request):
        appid = request.GET['appid'].encode("utf-8")
        type = request.GET['type'].encode("utf-8")
        content = {
            'type': type
        }
        if len(appid) == 18:
            return render(request, 'push/list.html', content)
        else:
            config.flash(request, "提示", "请先选择游戏或检查当前游戏wxAppId正确性")
            return render(request, 'message.html')

    @classmethod
    def handleLook(cls, request):
        id = request.GET['id'].encode("utf-8")
        type_id = request.GET['type'].encode("utf-8")
        look_all = {}

        func = ORIENTED_TYPE_GET_ALL_FUNC.get(type_id)
        if func:
            look_all, _ = func(id)

        return HttpResponse(json.dumps(look_all, indent=4, ensure_ascii=False, separators=(',', ':')),
                            content_type="application/json,charset=utf-8")

    @classmethod
    def handlePushOnline(cls, request):
        basic_id = request.GET['id'].encode("utf-8")
        type_id = request.GET['type'].encode("utf-8")
        obj = get_curr_oriented(int(basic_id), type_id)
        socket_url = config.getSocketUrl(obj[0].socket_url)

        try:
            if socket_url:
                func = ORIENTED_TYPE_GET_ALL_FUNC.get(type_id)
                if not func:
                    raise 'func is error %s %s' % (basic_id, type_id)

                get_all_data, wxAppIdList = func(basic_id)

                api_url = socket_url + config.gain_SetSocketApi(obj[0].socket_url)
                values = {
                    'versionId': int(basic_id),
                    'typeId': ORIENTED_TYPE_SERVER_ID[type_id],
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
                    # 处理推送显示
                    values.pop('oriented')
                    test_url = socket_url + config.gain_GetSocketApi(obj[0].socket_url) + "?" + urllib.urlencode(values)

                    info = {
                        'info': '成功',
                        'url': test_url,
                        'navigateToMiniProgramAppIdList': wxAppIdList,
                        'educeGameName': [game.allGame.get(i, '') for i in wxAppIdList]
                    }
                    # 处理操作人和操作时间
                    handle_userAndTime(basic_id, type_id)

                else:
                    info = {'info': '失败', 'code': html.get('code')}
            else:
                raise 'socketList is error %s %s' % (basic_id, type_id)
        except Exception, e:
            info = {'info': '失败! %s' % e}

        return HttpResponse(json.dumps(info, indent=4, ensure_ascii=False, separators=(',', ':')),
                            content_type="application/json,charset=utf-8")

    @classmethod
    def handleLookOnline(cls, request):
        basic_id = request.GET['id'].encode("utf-8")
        type_id = request.GET['type'].encode("utf-8")
        obj = get_curr_oriented(basic_id, type_id)
        socket_url = config.getSocketUrl(obj[0].socket_url)

        try:
            if socket_url:

                api_url = socket_url + config.gain_GetSocketApi(obj[0].socket_url)
                values = {
                    'typeId': ORIENTED_TYPE_SERVER_ID[type_id],
                    'gameId': obj[0].game_id,
                    'versionId': int(basic_id)
                }

                # 进行参数封装
                data = urllib.urlencode(values)
                # 组装完整url
                req = urllib2.Request(api_url, data)
                # 访问完整url
                response = urllib2.urlopen(req)
                info = eval(response.read())

            else:
                raise 'socketList is error %s %s' % (basic_id, type_id)
        except Exception, e:
            info = {'info': '失败! %s' % e}

        return HttpResponse(json.dumps(info, indent=4, ensure_ascii=False, separators=(',', ':')),
                            content_type="application/json,charset=utf-8")

