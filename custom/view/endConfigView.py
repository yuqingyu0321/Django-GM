# -*- coding: utf-8 -*-
'''
结束页配置
'''
import json

from django.http import HttpResponse
from django.shortcuts import render

from common import config
from custom.view.view import ViewHelper
from gameInfo import game
from gameInfo.models import *
from oriented.models import EndModel, GameEndModel, BgEndModel


class EndConfig(ViewHelper):
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
        allData = EndModel.objects.filter(name=appid)
        for _temp in allData:
            gameInfo = GameEndModel.objects.filter(foreignkey_EndModel=_temp.id)
            educeGame = [game.allGame.get(i.openUrl, i.openUrl) for i in gameInfo]
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
            return render(request, 'custom/endConfig/list.html')
        else:
            config.flash(request, "提示", "请先选择游戏或检查当前游戏wxAppId正确性")
            return render(request, 'message.html')

    @classmethod
    def handleAdd(cls, request):
        return render(request, 'custom/endConfig/add.html')

    @classmethod
    def handleSave(cls, request):
        appid = request.GET['appid'].encode("utf-8")

        reddot = request.GET['reddot'].encode("utf-8")
        viewAdCounts = request.GET['viewAdCounts'].encode("utf-8")
        switch = request.GET['switch'].encode("utf-8")

        gameObj = GameInfoModel.objects.get(wxAppid=appid)

        obj = EndModel()
        obj.name = gameObj.wxAppid
        obj.game_id = int(gameObj.game_id)
        obj.wxAppid = appid
        obj.socket_url = int(gameObj.socket_url)
        obj.reddot = reddot

        obj.viewAdCounts = viewAdCounts
        obj.switch = switch
        obj.save()

        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleLook(cls, request):
        id = request.GET.get('id')
        basic_data = EndModel.objects.filter(id=int(id))
        content = {
            'data': basic_data
        }
        return render(request, 'custom/endConfig/update.html', content)

    @classmethod
    def handleUpdate(cls, request):
        id = request.GET.get('id').encode("utf-8")
        reddot = request.GET['reddot'].encode("utf-8")
        viewAdCounts = request.GET['viewAdCounts'].encode("utf-8")
        switch = request.GET['switch'].encode("utf-8")
        EndModel.objects.filter(id=int(id)).update(reddot=reddot,
                                                   viewAdCounts=viewAdCounts,
                                                   switch=switch)

        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleDel(cls, request):
        id = request.GET.get('id').encode("utf-8")
        obj = EndModel.objects.get(id=int(id))
        # 删除子节点数据
        GameEndModel.objects.filter(foreignkey_EndModel=int(id)).delete()
        BgEndModel.objects.filter(foreignkey_EndModel=int(id)).delete()
        # 删除父节点数据
        EndModel.objects.filter(id=int(id)).delete()

        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleDelAll(cls, request):
        res = {}
        idstring = request.GET.get('data').encode("utf-8")
        if idstring:
            # 删除子节点数据
            GameEndModel.objects.extra(where=['foreignkey_EndModel_id IN (' + idstring + ')']).delete()
            BgEndModel.objects.extra(where=['foreignkey_EndModel_id IN (' + idstring + ')']).delete()
            # 删除父节点数据
            EndModel.objects.extra(where=['id IN (' + idstring + ')']).delete()
            res['code'] = 1
        else:
            res['code'] = 0
            res['msg'] = '请选择有效值'

        return HttpResponse(json.dumps(res))

    @classmethod
    def handleCopy(cls, request):
        id = request.GET['id'].encode("utf-8")
        # 获取父表数据
        obj = EndModel.objects.get(id=int(id))
        # 获取子表数据
        objBgChilds = BgEndModel.objects.filter(foreignkey_EndModel=obj)
        objChilds = GameEndModel.objects.filter(foreignkey_EndModel=obj)
        obj.id = None
        obj.save()
        for _temp in objChilds:
            _temp.id = None
            _temp.foreignkey_EndModel = obj
            _temp.save()
        for _tempPosi in objBgChilds:
            _tempPosi.id = None
            _tempPosi.foreignkey_EndModel = obj
            _tempPosi.save()
        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def _BgUpdataData(cls, request):
        fId = request.GET.get('id').encode("utf-8")
        # 背景数据
        # label 4
        label_height = request.GET['label_height'].encode("utf-8")
        label_scale = request.GET['label_scale'].encode("utf-8")
        label_yfromtop = request.GET['label_yfromtop'].encode("utf-8")
        label_imgurl = request.GET['label_imgurl'].encode("utf-8")

        # bg 4
        bg_width = request.GET['bg_width'].encode("utf-8")
        bg_height = request.GET['bg_height'].encode("utf-8")
        bg_positionY = request.GET['bg_positionY'].encode("utf-8")
        bg_imgurl = request.GET['bg_imgurl'].encode("utf-8")

        # gird 2
        grid_iconsWidth = request.GET['grid_iconsWidth'].encode("utf-8")
        grid_iconsHeight = request.GET['grid_iconsHeight'].encode("utf-8")

        BgEndModel.objects.filter(foreignkey_EndModel=int(fId)).update(
            label_height=label_height,
            label_scale=label_scale,
            label_yfromtop=label_yfromtop,
            label_imgurl=label_imgurl,
            bg_width=bg_width,
            bg_height=bg_height,
            bg_positionY=bg_positionY,
            bg_imgurl=bg_imgurl,
            grid_iconsWidth=grid_iconsWidth,
            grid_iconsHeight=grid_iconsHeight,
        )
        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def _BgAddData(cls, request):
        fId = request.GET.get('id').encode("utf-8")
        # 背景数据
        # label 4
        label_height = request.GET['label_height'].encode("utf-8")
        label_scale = request.GET['label_scale'].encode("utf-8")
        label_yfromtop = request.GET['label_yfromtop'].encode("utf-8")
        label_imgurl = request.GET['label_imgurl'].encode("utf-8")

        # bg 4
        bg_width = request.GET['bg_width'].encode("utf-8")
        bg_height = request.GET['bg_height'].encode("utf-8")
        bg_positionY = request.GET['bg_positionY'].encode("utf-8")
        bg_imgurl = request.GET['bg_imgurl'].encode("utf-8")

        # gird 2
        grid_iconsWidth = request.GET['grid_iconsWidth'].encode("utf-8")
        grid_iconsHeight = request.GET['grid_iconsHeight'].encode("utf-8")

        bgObj = BgEndModel(foreignkey_EndModel_id=int(fId))
        bgObj.label_height = label_height
        bgObj.label_scale = label_scale
        bgObj.label_yfromtop = label_yfromtop
        bgObj.label_imgurl = label_imgurl
        bgObj.bg_width = bg_width
        bgObj.bg_height = bg_height
        bgObj.bg_positionY = bg_positionY
        bgObj.bg_imgurl = bg_imgurl
        bgObj.grid_iconsWidth = grid_iconsWidth
        bgObj.grid_iconsHeight = grid_iconsHeight

        bgObj.save()
        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleBgLook(cls, request):
        id = request.GET.get('id')
        basic_data = BgEndModel.objects.filter(foreignkey_EndModel=int(id))
        content = {
            'data': basic_data,
            'fId': id
        }
        return render(request, 'custom/endConfig/bg/update.html', content)

    @classmethod
    def handleBgUpdate(cls, request):
        fId = request.GET.get('id').encode("utf-8")
        isCreate = BgEndModel.objects.filter(foreignkey_EndModel=int(fId)).count()

        return cls._BgUpdataData(request) if isCreate else cls._BgAddData(request)


class EndConfigSub(ViewHelper):
    @classmethod
    def handleData(cls, request):
        id = request.GET['id'].encode("utf-8")
        page = request.GET['page'].encode("utf-8")
        limit = request.GET['limit'].encode("utf-8")
        resData = []
        allData = GameEndModel.objects.filter(foreignkey_EndModel=int(id))
        index = 1
        for _temp in allData:
            _node = {
                'id': _temp.id,
                'index': _temp.index,
                'name': game.allGame.get(_temp.openUrl, _temp.openUrl),
            }
            resData.append(_node)
            index += 1
            print _temp.index

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
        return render(request, 'custom/endConfig/sub/list.html', content)

    @classmethod
    def handleAdd(cls, request):
        id = request.GET.get('id').encode("utf-8")
        content = {
            'fId': id,
            'gameChoice': game.allGame
        }
        return render(request, 'custom/endConfig/sub/add.html', content)

    @classmethod
    def handleSave(cls, request):
        id = request.GET['id'].encode("utf-8")
        index = request.GET['index'].encode("utf-8")
        text = request.GET['text'].encode("utf-8")
        type = request.GET['type'].encode("utf-8")
        imgLink = request.GET['imgLink'].encode("utf-8")
        openType = request.GET['openType'].encode("utf-8")
        openUrl = request.GET['wxAppId'].encode("utf-8")
        isredon = request.GET['isredon'].encode("utf-8")
        topath = request.GET['topath'].encode("utf-8")

        bi_iconId = request.GET['bi_iconId'].encode("utf-8")
        bi_landing_page = request.GET['bi_landing_page'].encode("utf-8")
        bi_landing_page_id = request.GET['bi_landing_page_id'].encode("utf-8")
        bi_educe_game = request.GET['bi_educe_game'].encode("utf-8")

        obj = EndModel.objects.get(id=id)
        gameObj = GameEndModel(foreignkey_EndModel=obj)
        gameObj.index = index
        gameObj.text = text
        gameObj.type = type
        gameObj.imgLink = imgLink
        gameObj.openType = openType
        gameObj.openUrl = openUrl
        gameObj.isredon = isredon
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
        basic_data = GameEndModel.objects.filter(id=int(id))
        content = {
            'data': basic_data,
            'gameChoice': game.allGame
        }
        return render(request, 'custom/endConfig/sub/update.html', content)

    @classmethod
    def handleUpdate(cls, request):
        id = request.GET.get('id').encode("utf-8")
        index = request.GET['index'].encode("utf-8")
        text = request.GET['text'].encode("utf-8")
        type = request.GET['type'].encode("utf-8")
        imgLink = request.GET['imgLink'].encode("utf-8")
        openType = request.GET['openType'].encode("utf-8")
        openUrl = request.GET['wxAppId'].encode("utf-8")
        isredon = request.GET['isredon'].encode("utf-8")
        topath = request.GET['topath'].encode("utf-8")

        bi_iconId = request.GET['bi_iconId'].encode("utf-8")
        bi_landing_page = request.GET['bi_landing_page'].encode("utf-8")
        bi_landing_page_id = request.GET['bi_landing_page_id'].encode("utf-8")
        bi_educe_game = request.GET['bi_educe_game'].encode("utf-8")

        GameEndModel.objects.filter(id=int(id)).update(index=index,
                                                             text=text,
                                                             type=type,
                                                             imgLink=imgLink,
                                                             openType=openType,
                                                             openUrl=openUrl,
                                                             isredon=isredon,
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

        GameEndModel.objects.filter(id=int(id)).delete()
        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleDelAll(cls, request):
        res = {}
        idstring = request.GET.get('data').encode("utf-8")
        if idstring:
            GameEndModel.objects.extra(where=['id IN (' + idstring + ')']).delete()
            res['code'] = 1
        else:
            res['code'] = 0
            res['msg'] = '请选择有效值'

        return HttpResponse(json.dumps(res))

    @classmethod
    def handleCopy(cls, request):
        id = request.GET['id'].encode("utf-8")
        # 获取子表数据
        obj = GameEndModel.objects.get(id=int(id))
        obj.id = None
        obj.save()
        return HttpResponse(json.dumps({
            "code": 1
        }))
