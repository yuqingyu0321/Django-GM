# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

import json
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import *
from gameInfo import game
game._init()


SOCKET_URL = {
    '0': '富豪服务器',
    '1': '三消服务器',
    '9999': '其他'
}

class GameInfoView(object):
    @classmethod
    def handleData(cls, request):
        page = request.GET['page'].encode("utf-8")
        limit = request.GET['limit'].encode("utf-8")
        resData = []
        allData = GameInfoModel.objects.all()
        for _temp in allData:
            _node = {
                'id': _temp.id,
                'name': _temp.name,
                'wxAppId': _temp.wxAppid,
                'innerGame': '是' if _temp.inner_game else '否',
                'socketUrl': SOCKET_URL.get(str(_temp.socket_url)),
                'gameId': _temp.game_id
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
        return render(request, 'gameInfo/list.html')

    @classmethod
    def handleAdd(cls, request):
        return render(request, 'gameInfo/add.html')

    @classmethod
    def handleSave(cls, request):

        name = request.GET.get('name').encode("utf-8")
        game_id = request.GET.get('gameId').encode("utf-8")
        wxAppid = request.GET.get('wxAppid').encode("utf-8")
        socket_url = request.GET.get('socket_url').encode("utf-8")
        inner_game = request.GET.get('inner_game').encode("utf-8")

        obj = GameInfoModel()
        obj.name = name
        obj.game_id = int(game_id)
        obj.wxAppid = wxAppid
        obj.socket_url = int(socket_url)
        obj.inner_game = int(inner_game)
        obj.save()
        game._addGame(obj)
        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleLook(cls, request):
        id = request.GET.get('id')
        basic_data = GameInfoModel.objects.filter(id=int(id))
        content = {
            'data': basic_data
        }
        return render(request, 'gameInfo/update.html', content)

    @classmethod
    def handleUpdate(cls, request):
        id = request.GET.get('id').encode("utf-8")
        name = request.GET.get('name').encode("utf-8")
        game_id = request.GET.get('gameId').encode("utf-8")
        wxAppid = request.GET.get('wxAppid').encode("utf-8")
        socket_url = request.GET.get('socket_url').encode("utf-8")
        inner_game = request.GET.get('inner_game').encode("utf-8")
        GameInfoModel.objects.filter(id=int(id)).update(name=name,
                                                        game_id=int(game_id),
                                                        wxAppid=wxAppid,
                                                        socket_url=int(socket_url),
                                                        inner_game=int(inner_game))
        obj = GameInfoModel.objects.get(id=int(id))
        game._addGame(obj)
        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleDel(cls, request):
        id = request.GET.get('id').encode("utf-8")
        obj = GameInfoModel.objects.get(id=int(id))
        game._removeGame(obj)
        GameInfoModel.objects.filter(id=int(id)).delete()
        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleDelAll(cls, request):
        res = {}
        idstring = request.GET.get('data').encode("utf-8")
        if idstring:
            objList = GameInfoModel.objects.extra(where=['id IN (' + idstring + ')'])
            game._removeAllGame(objList)
            GameInfoModel.objects.extra(where=['id IN (' + idstring + ')']).delete()
            res['code'] = 1
        else:
            res['code'] = 0
            res['msg'] = '请选择有效值'

        return HttpResponse(json.dumps(res))
