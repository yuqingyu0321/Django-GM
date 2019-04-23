# -*- coding: utf-8 -*-
'''
导流条配置
'''
import json
from django.shortcuts import render
from common import config
from oriented.models import GameStripModel, StripModel
from gameInfo.models import *
from django.http import HttpResponse
from gameInfo import game
from custom.view.view import ViewHelper


class StripConfig(ViewHelper):
    @classmethod
    def handleData(cls, request):
        appid = request.GET['appid'].encode("utf-8")
        if len(appid) == 18:
            pass
        else:
            config.flash(request, "提示", "请先选择游戏或检查当前游戏wxAppId正确性")
            return render(request, 'message.html')

        page = request.GET['page'].encode("utf-8")
        limit = request.GET['limit'].encode("utf-8")
        resData = []
        allData = StripModel.objects.filter(name=appid)
        for _temp in allData:
            gameInfo = GameStripModel.objects.filter(foreignkey_strip=int(_temp.id))
            educeGame = [game.allGame.get(i.wxAppId, i.wxAppId) for i in gameInfo]
            _node = {
                'id': _temp.id,
                'name': game.innerGame.get(_temp.name, ''),
                'educeGame': educeGame,
                'educeGameCount': len(educeGame),
                'modifiTime': _temp.modifi_time.strftime('%Y-%m-%d %H:%M:%S.%f')
            }
            resData.append(_node)

        startIndex = (int(page) - 1) * int(limit)
        if startIndex + int(limit) - 1 < len(resData):
            endIndex = startIndex + int(limit) - 1
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
        if len(appid) == 18:
            return render(request, 'custom/stripConfig/list.html')
        else:
            config.flash(request, "提示", "请先选择游戏或检查当前游戏wxAppId正确性")
            return render(request, 'message.html')

    @classmethod
    def handleAdd(cls, request):
        return render(request, 'custom/stripConfig/add.html')

    @classmethod
    def handleSave(cls, request):
        appid = request.GET['appid'].encode("utf-8")
        label = request.GET['label'].encode("utf-8")
        bg = request.GET['bg'].encode("utf-8")
        reddot = request.GET['reddot'].encode("utf-8")
        spacingX = request.GET['spacingX'].encode("utf-8")
        iconWidth = request.GET['iconWidth'].encode("utf-8")
        iconHeight = request.GET['iconHeight'].encode("utf-8")
        switch = request.GET['switch'].encode("utf-8")
        viewAdCounts = request.GET['viewAdCounts'].encode("utf-8")
        framesInterval = request.GET['framesInterval'].encode("utf-8")

        gameObj = GameInfoModel.objects.get(wxAppid=appid)

        obj = StripModel()
        obj.name = gameObj.wxAppid
        obj.game_id = int(gameObj.game_id)
        obj.wxAppid = appid
        obj.socket_url = int(gameObj.socket_url)
        obj.label = label
        obj.bg = bg
        obj.reddot = reddot
        obj.spacingX = spacingX
        obj.iconWidth = iconWidth
        obj.iconHeight = iconHeight
        obj.switch = switch
        obj.viewAdCounts = viewAdCounts
        obj.framesInterval = framesInterval
        obj.save()

        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleLook(cls, request):
        id = request.GET.get('id')
        basic_data = StripModel.objects.filter(id=int(id))
        content = {
            'data': basic_data
        }
        return render(request, 'custom/stripConfig/update.html', content)

    @classmethod
    def handleUpdate(cls, request):
        id = request.GET.get('id').encode("utf-8")
        label = request.GET['label'].encode("utf-8")
        bg = request.GET['bg'].encode("utf-8")
        reddot = request.GET['reddot'].encode("utf-8")
        spacingX = request.GET['spacingX'].encode("utf-8")
        iconWidth = request.GET['iconWidth'].encode("utf-8")
        iconHeight = request.GET['iconHeight'].encode("utf-8")
        switch = request.GET['switch'].encode("utf-8")
        viewAdCounts = request.GET['viewAdCounts'].encode("utf-8")
        framesInterval = request.GET['framesInterval'].encode("utf-8")

        StripModel.objects.filter(id=int(id)).update(label=label,
                                                     bg=bg,
                                                     reddot=reddot,
                                                     spacingX=spacingX,
                                                     iconWidth=iconWidth,
                                                     iconHeight=iconHeight,
                                                     switch=switch,
                                                     viewAdCounts=viewAdCounts,
                                                     framesInterval=framesInterval)

        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleDel(cls, request):
        id = request.GET.get('id').encode("utf-8")
        obj = StripModel.objects.get(id=int(id))
        # 删除子节点数据
        GameStripModel.objects.filter(foreignkey_strip=int(id)).delete()

        # 删除父节点数据
        StripModel.objects.filter(id=int(id)).delete()

        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleDelAll(cls, request):
        res = {}
        idstring = request.GET.get('data').encode("utf-8")
        if idstring:
            # 删除子节点数据
            GameStripModel.objects.extra(where=['foreignkey_strip_id IN (' + idstring + ')']).delete()

            # 删除父节点数据
            StripModel.objects.extra(where=['id IN (' + idstring + ')']).delete()
            res['code'] = 1
        else:
            res['code'] = 0
            res['msg'] = '请选择有效值'

        return HttpResponse(json.dumps(res))

    @classmethod
    def handleCopy(cls, request):
        id = request.GET['id'].encode("utf-8")
        # 获取父表数据
        obj = StripModel.objects.get(id=int(id))
        # 获取子表数据
        objChilds = GameStripModel.objects.filter(foreignkey_strip_id=obj)
        obj.id = None
        obj.save()
        for _temp in objChilds:
            _temp.id = None
            _temp.foreignkey_strip_id = obj
            _temp.save()

        return HttpResponse(json.dumps({
            "code": 1
        }))


class StripSub(ViewHelper):
    @classmethod
    def handleData(cls, request):
        id = request.GET['id'].encode("utf-8")
        page = request.GET['page'].encode("utf-8")
        limit = request.GET['limit'].encode("utf-8")
        resData = []
        allData = GameStripModel.objects.filter(foreignkey_strip=int(id))
        for _temp in allData:
            _node = {
                'id': _temp.id,
                'name': game.allGame.get(_temp.wxAppId, _temp.wxAppId),
            }
            resData.append(_node)

        startIndex = (int(page) - 1) * int(limit)
        if startIndex + int(limit) - 1 < len(resData):
            endIndex = startIndex + int(limit) - 1
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
        id = request.GET.get('id').encode("utf-8")
        content = {'fId': id}
        return render(request, 'custom/stripConfig/sub/list.html', content)

    @classmethod
    def handleAdd(cls, request):
        id = request.GET.get('id').encode("utf-8")
        content = {
            'fId': id,
            'gameChoice': game.allGame
        }
        return render(request, 'custom/stripConfig/sub/add.html', content)

    @classmethod
    def handleSave(cls, request):
        id = request.GET['id'].encode("utf-8")
        wxAppId = request.GET['wxAppId'].encode("utf-8")
        index = request.GET['index'].encode("utf-8")
        imgLink = request.GET['imgLink'].encode("utf-8")
        isClickHide = request.GET['isClickHide'].encode("utf-8")
        topath = request.GET['topath'].encode("utf-8")

        bi_iconId = request.GET['bi_iconId'].encode("utf-8")
        bi_landing_page = request.GET['bi_landing_page'].encode("utf-8")
        bi_landing_page_id = request.GET['bi_landing_page_id'].encode("utf-8")
        bi_educe_game = request.GET['bi_educe_game'].encode("utf-8")

        obj = StripModel.objects.get(id=id)
        gameObj = GameStripModel(foreignkey_strip=obj)
        gameObj.wxAppId = wxAppId
        gameObj.index = index
        gameObj.imgLink = imgLink
        gameObj.isClickHide = isClickHide
        gameObj.topath = topath
        gameObj.bi_iconId = bi_iconId
        gameObj.bi_landing_page = bi_landing_page
        gameObj.bi_landing_page_id = bi_landing_page_id
        gameObj.bi_educe_game = bi_educe_game
        gameObj.save()
        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleLook(cls, request):
        id = request.GET.get('id')
        basic_data = GameStripModel.objects.filter(id=int(id))
        content = {
            'data': basic_data,
            'gameChoice': game.allGame
        }
        return render(request, 'custom/stripConfig/sub/update.html', content)

    @classmethod
    def handleUpdate(cls, request):
        id = request.GET.get('id').encode("utf-8")
        wxAppId = request.GET['wxAppId'].encode("utf-8")
        index = request.GET['index'].encode("utf-8")
        imgLink = request.GET['imgLink'].encode("utf-8")
        isClickHide = request.GET['isClickHide'].encode("utf-8")
        topath = request.GET['topath'].encode("utf-8")

        bi_iconId = request.GET['bi_iconId'].encode("utf-8")
        bi_landing_page = request.GET['bi_landing_page'].encode("utf-8")
        bi_landing_page_id = request.GET['bi_landing_page_id'].encode("utf-8")
        bi_educe_game = request.GET['bi_educe_game'].encode("utf-8")

        GameStripModel.objects.filter(id=int(id)).update(wxAppId=wxAppId,
                                                         index=index,
                                                         imgLink=imgLink,
                                                         isClickHide=isClickHide,
                                                         topath=topath,
                                                         bi_iconId=bi_iconId,
                                                         bi_landing_page=bi_landing_page,
                                                         bi_landing_page_id=bi_landing_page_id,
                                                         bi_educe_game=bi_educe_game)

        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleDel(cls, request):
        id = request.GET.get('id').encode("utf-8")

        GameStripModel.objects.filter(id=int(id)).delete()
        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleDelAll(cls, request):
        res = {}
        idstring = request.GET.get('data').encode("utf-8")
        if idstring:
            GameStripModel.objects.extra(where=['id IN (' + idstring + ')']).delete()
            res['code'] = 1
        else:
            res['code'] = 0
            res['msg'] = '请选择有效值'

        return HttpResponse(json.dumps(res))

    @classmethod
    def handleCopy(cls, request):
        id = request.GET['id'].encode("utf-8")
        # 获取子表数据
        obj = GameStripModel.objects.get(id=int(id))
        obj.id = None
        obj.save()
        return HttpResponse(json.dumps({
            "code": 1
        }))
