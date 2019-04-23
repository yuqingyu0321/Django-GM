# -*- coding: utf-8 -*-
'''
Icon配置
'''
import json
from django.shortcuts import render
from common import config
from oriented.models import PositionModel,GameIconSwitchModel, IconSwitchModel
from gameInfo.models import *
from django.http import HttpResponse
from gameInfo import game
from custom.view.view import ViewHelper

class OrientedIconConfig(ViewHelper):
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
        allData = IconSwitchModel.objects.filter(name=appid)
        for _temp in allData:
            gameInfo = GameIconSwitchModel.objects.filter(foreignkey_iconswitch=_temp.id)
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
        if len(appid) == 18:
            return render(request, 'custom/iconConfig/list.html')
        else:
            config.flash(request, "提示", "请先选择游戏或检查当前游戏wxAppId正确性")
            return render(request, 'message.html')

    @classmethod
    def handleAdd(cls, request):
        return render(request, 'custom/iconConfig/add.html')

    @classmethod
    def handleSave(cls, request):
        appid = request.GET['appid'].encode("utf-8")
        switch = request.GET['switch'].encode("utf-8")
        framesInterval = request.GET['framesInterval'].encode("utf-8")

        gameObj = GameInfoModel.objects.get(wxAppid=appid)

        obj = IconSwitchModel()
        obj.name = gameObj.wxAppid
        obj.game_id = int(gameObj.game_id)
        obj.wxAppid = appid
        obj.socket_url = int(gameObj.socket_url)
        obj.switch = switch
        obj.framesInterval = framesInterval
        obj.save()

        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleLook(cls, request):
        id = request.GET.get('id')
        basic_data = IconSwitchModel.objects.filter(id=int(id))
        content = {
            'data': basic_data
        }
        return render(request, 'custom/iconConfig/update.html', content)

    @classmethod
    def handleUpdate(cls, request):
        id = request.GET.get('id').encode("utf-8")
        switch = request.GET['switch'].encode("utf-8")
        framesInterval = request.GET['framesInterval'].encode("utf-8")
        IconSwitchModel.objects.filter(id=int(id)).update(switch=switch,
                                                          framesInterval=framesInterval)

        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleDel(cls, request):
        id = request.GET.get('id').encode("utf-8")
        obj = IconSwitchModel.objects.get(id=int(id))
        # 删除子节点数据
        GameIconSwitchModel.objects.filter(foreignkey_iconswitch=int(id)).delete()
        PositionModel.objects.filter(foreignkey_iconswitch=int(id)).delete()
        # 删除父节点数据
        IconSwitchModel.objects.filter(id=int(id)).delete()

        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleDelAll(cls, request):
        res = {}
        idstring = request.GET.get('data').encode("utf-8")
        if idstring:
            # 删除子节点数据
            GameIconSwitchModel.objects.extra(where=['foreignkey_iconswitch_id IN (' + idstring + ')']).delete()
            PositionModel.objects.extra(where=['foreignkey_iconswitch_id IN (' + idstring + ')']).delete()
            # 删除父节点数据
            IconSwitchModel.objects.extra(where=['id IN (' + idstring + ')']).delete()
            res['code'] = 1
        else:
            res['code'] = 0
            res['msg'] = '请选择有效值'

        return HttpResponse(json.dumps(res))

    @classmethod
    def handleCopy(cls, request):
        id = request.GET['id'].encode("utf-8")
        # 获取父表数据
        obj = IconSwitchModel.objects.get(id=int(id))
        # 获取子表数据
        objPositionChilds = PositionModel.objects.filter(foreignkey_iconswitch=obj)
        objChilds = GameIconSwitchModel.objects.filter(foreignkey_iconswitch=obj)
        obj.id = None
        obj.save()
        for _temp in objChilds:
            _temp.id = None
            _temp.foreignkey_iconswitch = obj
            _temp.save()
        for _tempPosi in objPositionChilds:
            _tempPosi.id = None
            _tempPosi.foreignkey_iconswitch = obj
            _tempPosi.save()
        return HttpResponse(json.dumps({
            "code": 1
        }))


class OrientedIconSub(ViewHelper):
    @classmethod
    def handleData(cls, request):
        id = request.GET['id'].encode("utf-8")
        page = request.GET['page'].encode("utf-8")
        limit = request.GET['limit'].encode("utf-8")
        resData = []
        allData = GameIconSwitchModel.objects.filter(foreignkey_iconswitch=int(id))
        index = 1
        for _temp in allData:
            _node = {
                'id': index,
                'name': game.allGame.get(_temp.wxAppId, _temp.wxAppId),
            }
            resData.append(_node)
            index += 1

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
        id = request.GET.get('id').encode("utf-8")
        content = {'fId': id}
        return render(request, 'custom/iconConfig/sub/list.html', content)

    @classmethod
    def handleAdd(cls, request):
        id = request.GET.get('id').encode("utf-8")
        content = {
            'fId': id,
            'gameChoice': game.allGame
        }
        return render(request, 'custom/iconConfig/sub/add.html', content)

    @classmethod
    def handleSave(cls, request):
        id = request.GET['id'].encode("utf-8")
        wxAppId = request.GET['wxAppId'].encode("utf-8")
        weight = request.GET['weight'].encode("utf-8")
        scale = request.GET['scale'].encode("utf-8")
        imgLink = request.GET['imgLink'].encode("utf-8")
        openType = request.GET['openType'].encode("utf-8")
        clickHide = request.GET['clickHide'].encode("utf-8")
        topath = request.GET['topath'].encode("utf-8")

        bi_iconId = request.GET['bi_iconId'].encode("utf-8")
        bi_landing_page = request.GET['bi_landing_page'].encode("utf-8")
        bi_landing_page_id = request.GET['bi_landing_page_id'].encode("utf-8")
        bi_educe_game = request.GET['bi_educe_game'].encode("utf-8")

        obj = IconSwitchModel.objects.get(id=id)
        gameObj = GameIconSwitchModel(foreignkey_iconswitch=obj)
        gameObj.wxAppId = wxAppId
        gameObj.weight = int(weight)
        gameObj.scale = float(scale)
        gameObj.imgLink = imgLink
        gameObj.openType = int(openType)
        gameObj.clickHide = int(clickHide)
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
        basic_data = GameIconSwitchModel.objects.filter(id=int(id))
        content = {
            'data': basic_data,
            'gameChoice': game.allGame
        }
        return render(request, 'custom/iconConfig/sub/update.html', content)

    @classmethod
    def handleUpdate(cls, request):
        id = request.GET.get('id').encode("utf-8")
        wxAppId = request.GET['wxAppId'].encode("utf-8")
        weight = request.GET['weight'].encode("utf-8")
        scale = request.GET['scale'].encode("utf-8")
        imgLink = request.GET['imgLink'].encode("utf-8")
        openType = request.GET['openType'].encode("utf-8")
        clickHide = request.GET['clickHide'].encode("utf-8")
        topath = request.GET['topath'].encode("utf-8")

        bi_iconId = request.GET['bi_iconId'].encode("utf-8")
        bi_landing_page = request.GET['bi_landing_page'].encode("utf-8")
        bi_landing_page_id = request.GET['bi_landing_page_id'].encode("utf-8")
        bi_educe_game = request.GET['bi_educe_game'].encode("utf-8")

        GameIconSwitchModel.objects.filter(id=int(id)).update(wxAppId=wxAppId,
                                                              weight=weight,
                                                              scale=scale,
                                                              imgLink=imgLink,
                                                              openType=openType,
                                                              clickHide=clickHide,
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

        GameIconSwitchModel.objects.filter(id=int(id)).delete()
        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleDelAll(cls, request):
        res = {}
        idstring = request.GET.get('data').encode("utf-8")
        if idstring:
            GameIconSwitchModel.objects.extra(where=['id IN (' + idstring + ')']).delete()
            res['code'] = 1
        else:
            res['code'] = 0
            res['msg'] = '请选择有效值'

        return HttpResponse(json.dumps(res))

    @classmethod
    def handleCopy(cls, request):
        id = request.GET['id'].encode("utf-8")
        # 获取子表数据
        obj = GameIconSwitchModel.objects.get(id=int(id))
        obj.id = None
        obj.save()
        return HttpResponse(json.dumps({
            "code": 1
        }))


class OrientedIconPosition(ViewHelper):
    @classmethod
    def handleData(cls, request):
        id = request.GET['id'].encode("utf-8")
        page = request.GET['page'].encode("utf-8")
        limit = request.GET['limit'].encode("utf-8")
        resData = []
        allData = PositionModel.objects.filter(foreignkey_iconswitch=int(id))
        for _temp in allData:
            _node = {
                'id': _temp.id,
                'position_id': _temp.position_id,
                'x': _temp.x,
                'y': _temp.y,
                'type': _temp.type
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
        id = request.GET.get('id').encode("utf-8")
        content = {'fId': id}
        return render(request, 'custom/iconConfig/position/list.html', content)

    @classmethod
    def handleAdd(cls, request):
        id = request.GET.get('id').encode("utf-8")
        content = {
            'fId': id
        }
        return render(request, 'custom/iconConfig/position/add.html', content)

    @classmethod
    def handleSave(cls, request):
        id = request.GET['id'].encode("utf-8")
        position_id = request.GET['position_id'].encode("utf-8")
        type = request.GET['type'].encode("utf-8")
        x = request.GET['x'].encode("utf-8")
        y = request.GET['y'].encode("utf-8")

        obj = IconSwitchModel.objects.get(id=int(id))
        positionObj = PositionModel(foreignkey_iconswitch=obj)
        positionObj.position_id = int(position_id)
        positionObj.type = int(type)
        positionObj.x = float(x)
        positionObj.y = float(y)
        positionObj.save()

        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleLook(cls, request):
        id = request.GET.get('id')
        basic_data = PositionModel.objects.filter(id=int(id))
        content = {
            'data': basic_data,
        }
        return render(request, 'custom/iconConfig/position/update.html', content)

    @classmethod
    def handleUpdate(cls, request):
        id = request.GET.get('id').encode("utf-8")
        position_id = request.GET['position_id'].encode("utf-8")
        type = request.GET['type'].encode("utf-8")
        x = request.GET['x'].encode("utf-8")
        y = request.GET['y'].encode("utf-8")

        PositionModel.objects.filter(id=int(id)).update(position_id=position_id,
                                                        type=type,
                                                        x=x,
                                                        y=y)

        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleDel(cls, request):
        id = request.GET.get('id').encode("utf-8")

        PositionModel.objects.filter(id=int(id)).delete()
        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleDelAll(cls, request):
        res = {}
        idstring = request.GET.get('data').encode("utf-8")
        if idstring:
            PositionModel.objects.extra(where=['id IN (' + idstring + ')']).delete()
            res['code'] = 1
        else:
            res['code'] = 0
            res['msg'] = '请选择有效值'

        return HttpResponse(json.dumps(res))

    @classmethod
    def handleCopy(cls, request):
        id = request.GET['id'].encode("utf-8")
        # 获取子表数据
        obj = PositionModel.objects.get(id=int(id))
        obj.id = None
        obj.save()
        return HttpResponse(json.dumps({
            "code": 1
        }))
