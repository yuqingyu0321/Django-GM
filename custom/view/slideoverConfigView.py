# -*- coding: utf-8 -*-
'''
侧拉框配置
'''
import json
from django.shortcuts import render
from common import config
from oriented.models import SlideOverModel, BgSlideOverModel, GameSlideOverModel
from gameInfo.models import *
from django.http import HttpResponse
from gameInfo import game
from custom.view.view import ViewHelper


class SlideoverConfig(ViewHelper):
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
        allData = SlideOverModel.objects.filter(name=appid)
        for _temp in allData:
            gameInfo = GameSlideOverModel.objects.filter(foreignkey_labelSlideOver=_temp.id)
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
            return render(request, 'custom/slideoverConfig/list.html')
        else:
            config.flash(request, "提示", "请先选择游戏或检查当前游戏wxAppId正确性")
            return render(request, 'message.html')

    @classmethod
    def handleAdd(cls, request):
        return render(request, 'custom/slideoverConfig/add.html')



    @classmethod
    def handleSave(cls, request):
        appid = request.GET['appid'].encode("utf-8")
        reddot = request.GET['reddot'].encode("utf-8")
        mask = request.GET['mask'].encode("utf-8")
        fromWhere = request.GET['fromWhere'].encode("utf-8")
        viewAdCounts = request.GET['viewAdCounts'].encode("utf-8")
        switch = request.GET['switch'].encode("utf-8")


        gameObj = GameInfoModel.objects.get(wxAppid=appid)

        obj = SlideOverModel()
        obj.name = gameObj.wxAppid
        obj.game_id = int(gameObj.game_id)
        obj.wxAppid = appid
        obj.socket_url = int(gameObj.socket_url)
        obj.reddot = reddot
        obj.mask = mask
        obj.fromWhere = fromWhere
        obj.viewAdCounts = viewAdCounts
        obj.switch = switch
        obj.save()

        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleLook(cls, request):
        id = request.GET.get('id')
        basic_data = SlideOverModel.objects.filter(id=int(id))
        content = {
            'data': basic_data
        }
        return render(request, 'custom/slideoverConfig/update.html', content)

    @classmethod
    def handleUpdate(cls, request):
        id = request.GET.get('id').encode("utf-8")
        reddot = request.GET['reddot'].encode("utf-8")
        mask = request.GET['mask'].encode("utf-8")
        fromWhere = request.GET['fromWhere'].encode("utf-8")
        viewAdCounts = request.GET['viewAdCounts'].encode("utf-8")
        switch = request.GET['switch'].encode("utf-8")
        SlideOverModel.objects.filter(id=int(id)).update(reddot=reddot,
                                                         mask=mask,
                                                         fromWhere=fromWhere,
                                                         viewAdCounts=viewAdCounts,
                                                         switch=switch)



        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleDel(cls, request):
        id = request.GET.get('id').encode("utf-8")
        obj = SlideOverModel.objects.get(id=int(id))
        # 删除子节点数据
        GameSlideOverModel.objects.filter(foreignkey_labelSlideOver=int(id)).delete()
        BgSlideOverModel.objects.filter(foreignkey_labelSlideOver=int(id)).delete()
        # 删除父节点数据
        SlideOverModel.objects.filter(id=int(id)).delete()

        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleDelAll(cls, request):
        res = {}
        idstring = request.GET.get('data').encode("utf-8")
        if idstring:
            # 删除子节点数据
            GameSlideOverModel.objects.extra(where=['foreignkey_labelSlideOver_id IN (' + idstring + ')']).delete()
            BgSlideOverModel.objects.extra(where=['foreignkey_labelSlideOver_id IN (' + idstring + ')']).delete()
            # 删除父节点数据
            SlideOverModel.objects.extra(where=['id IN (' + idstring + ')']).delete()
            res['code'] = 1
        else:
            res['code'] = 0
            res['msg'] = '请选择有效值'

        return HttpResponse(json.dumps(res))

    @classmethod
    def handleCopy(cls, request):
        id = request.GET['id'].encode("utf-8")
        # 获取父表数据
        obj = SlideOverModel.objects.get(id=int(id))
        # 获取子表数据
        objPositionChilds = BgSlideOverModel.objects.filter(foreignkey_labelSlideOver=obj)
        objChilds = GameSlideOverModel.objects.filter(foreignkey_labelSlideOver=obj)
        obj.id = None
        obj.save()
        for _temp in objChilds:
            _temp.id = None
            _temp.foreignkey_labelSlideOver = obj
            _temp.save()
        for _tempPosi in objPositionChilds:
            _tempPosi.id = None
            _tempPosi.foreignkey_labelSlideOver = obj
            _tempPosi.save()
        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def _BgUpdataData(cls, request):
        fId = request.GET.get('id').encode("utf-8")
        # 背景数据
        # 标题 4
        bt_height = request.GET['bt_height'].encode("utf-8")
        bt_scale = request.GET['bt_scale'].encode("utf-8")
        bt_yfromtop = request.GET['bt_yfromtop'].encode("utf-8")
        bt_imgurl = request.GET['bt_imgurl'].encode("utf-8")

        # 框 3
        kuang_positionY = request.GET['kuang_positionY'].encode("utf-8")
        kuang_bottomBlkHeight = request.GET['kuang_bottomBlkHeight'].encode("utf-8")
        kuang_imgurl = request.GET['kuang_imgurl'].encode("utf-8")

        # 拉按钮 6
        la_scale = request.GET['la_scale'].encode("utf-8")
        la_positionX = request.GET['la_positionX'].encode("utf-8")
        la_positionY = request.GET['la_positionY'].encode("utf-8")
        la_imgurl0 = request.GET['la_imgurl0'].encode("utf-8")
        la_imgurl1 = request.GET['la_imgurl1'].encode("utf-8")
        la_isredon = request.GET['la_isredon'].encode("utf-8")

        # icon布局 6
        icon_iconsWidth = request.GET['icon_iconsWidth'].encode("utf-8")
        icon_iconsHeight = request.GET['icon_iconsHeight'].encode("utf-8")
        icon_spacingX = request.GET['icon_spacingX'].encode("utf-8")
        icon_spacingY = request.GET['icon_spacingY'].encode("utf-8")
        icon_paddingLeft = request.GET['icon_paddingLeft'].encode("utf-8")
        icon_paddingRight = request.GET['icon_paddingRight'].encode("utf-8")

        # 文本 5
        text_size = request.GET['text_size'].encode("utf-8")
        text_yfromIcon = request.GET['text_yfromIcon'].encode("utf-8")
        text_colorR = request.GET['text_colorR'].encode("utf-8")
        text_colorG = request.GET['text_colorG'].encode("utf-8")
        text_colorB = request.GET['text_colorB'].encode("utf-8")

        BgSlideOverModel.objects.filter(foreignkey_labelSlideOver=int(fId)).update(
            bt_height=bt_height,
            bt_scale=bt_scale,
            bt_yfromtop=bt_yfromtop,
            bt_imgurl=bt_imgurl,
            kuang_positionY=kuang_positionY,
            kuang_bottomBlkHeight=kuang_bottomBlkHeight,
            kuang_imgurl=kuang_imgurl,
            la_scale=la_scale,
            la_positionX=la_positionX,
            la_positionY=la_positionY,
            la_imgurl0=la_imgurl0,
            la_imgurl1=la_imgurl1,
            la_isredon=la_isredon,
            icon_iconsWidth=icon_iconsWidth,
            icon_iconsHeight=icon_iconsHeight,
            icon_spacingX=icon_spacingX,
            icon_spacingY=icon_spacingY,
            icon_paddingRight=icon_paddingRight,
            text_size=text_size,
            text_yfromIcon=text_yfromIcon,
            text_colorR=text_colorR,
            text_colorG=text_colorG,
            text_colorB=text_colorB,
        )
        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def _BgAddData(cls, request):
        fId = request.GET.get('id').encode("utf-8")
        # 背景数据
        # 标题 4
        bt_height = request.GET['bt_height'].encode("utf-8")
        bt_scale = request.GET['bt_scale'].encode("utf-8")
        bt_yfromtop = request.GET['bt_yfromtop'].encode("utf-8")
        bt_imgurl = request.GET['bt_imgurl'].encode("utf-8")

        # 框 3
        kuang_positionY = request.GET['kuang_positionY'].encode("utf-8")
        kuang_bottomBlkHeight = request.GET['kuang_bottomBlkHeight'].encode("utf-8")
        kuang_imgurl = request.GET['kuang_imgurl'].encode("utf-8")

        # 拉按钮 6
        la_scale = request.GET['la_scale'].encode("utf-8")
        la_positionX = request.GET['la_positionX'].encode("utf-8")
        la_positionY = request.GET['la_positionY'].encode("utf-8")
        la_imgurl0 = request.GET['la_imgurl0'].encode("utf-8")
        la_imgurl1 = request.GET['la_imgurl1'].encode("utf-8")
        la_isredon = request.GET['la_isredon'].encode("utf-8")

        # icon布局 6
        icon_iconsWidth = request.GET['icon_iconsWidth'].encode("utf-8")
        icon_iconsHeight = request.GET['icon_iconsHeight'].encode("utf-8")
        icon_spacingX = request.GET['icon_spacingX'].encode("utf-8")
        icon_spacingY = request.GET['icon_spacingY'].encode("utf-8")
        icon_paddingLeft = request.GET['icon_paddingLeft'].encode("utf-8")
        icon_paddingRight = request.GET['icon_paddingRight'].encode("utf-8")

        # 文本 5
        text_size = request.GET['text_size'].encode("utf-8")
        text_yfromIcon = request.GET['text_yfromIcon'].encode("utf-8")
        text_colorR = request.GET['text_colorR'].encode("utf-8")
        text_colorG = request.GET['text_colorG'].encode("utf-8")
        text_colorB = request.GET['text_colorB'].encode("utf-8")

        bgObj = BgSlideOverModel(foreignkey_labelSlideOver_id=int(fId))
        bgObj.bt_height = bt_height
        bgObj.bt_scale = bt_scale
        bgObj.bt_yfromtop = bt_yfromtop
        bgObj.bt_imgurl = bt_imgurl

        bgObj.kuang_positionY = kuang_positionY
        bgObj.kuang_bottomBlkHeight = kuang_bottomBlkHeight
        bgObj.kuang_imgurl = kuang_imgurl

        bgObj.la_scale = la_scale
        bgObj.la_positionX = la_positionX
        bgObj.la_positionY = la_positionY
        bgObj.la_imgurl0 = la_imgurl0
        bgObj.la_imgurl1 = la_imgurl1
        bgObj.la_isredon = la_isredon

        bgObj.icon_iconsWidth = icon_iconsWidth
        bgObj.icon_iconsHeight = icon_iconsHeight
        bgObj.icon_spacingX = icon_spacingX
        bgObj.icon_spacingY = icon_spacingY
        bgObj.icon_paddingLeft = icon_paddingLeft
        bgObj.icon_paddingRight = icon_paddingRight

        bgObj.text_size = text_size
        bgObj.text_yfromIcon = text_yfromIcon
        bgObj.text_colorR = text_colorR
        bgObj.text_colorG = text_colorG
        bgObj.text_colorB = text_colorB

        bgObj.save()
        return HttpResponse(json.dumps({
                    "code": 1
                }))
    @classmethod
    def handleBgLook(cls, request):
        id = request.GET.get('id')
        basic_data = BgSlideOverModel.objects.filter(foreignkey_labelSlideOver=int(id))
        content = {
            'data': basic_data,
            'fId': id
        }
        return render(request, 'custom/slideoverConfig/bg/update.html', content)

    @classmethod
    def handleBgUpdate(cls, request):
        fId = request.GET.get('id').encode("utf-8")
        isCreate = BgSlideOverModel.objects.filter(foreignkey_labelSlideOver=int(fId)).count()

        return cls._BgUpdataData(request) if isCreate else cls._BgAddData(request)



class SlideoverSub(ViewHelper):
    @classmethod
    def handleData(cls, request):
        id = request.GET['id'].encode("utf-8")
        page = request.GET['page'].encode("utf-8")
        limit = request.GET['limit'].encode("utf-8")
        resData = []
        allData = GameSlideOverModel.objects.filter(foreignkey_labelSlideOver=int(id))
        index = 1
        for _temp in allData:
            _node = {
                'id': index,
                'index': _temp.index,
                'name': game.allGame.get(_temp.openUrl, _temp.openUrl),
            }
            resData.append(_node)
            index += 1

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
        return render(request, 'custom/slideoverConfig/sub/list.html', content)

    @classmethod
    def handleAdd(cls, request):
        id = request.GET.get('id').encode("utf-8")
        content = {
            'fId': id,
            'gameChoice': game.allGame
        }
        return render(request, 'custom/slideoverConfig/sub/add.html', content)

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

        obj = SlideOverModel.objects.get(id=id)
        gameObj = GameSlideOverModel(foreignkey_labelSlideOver=obj)
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
        basic_data = GameSlideOverModel.objects.filter(id=int(id))
        content = {
            'data': basic_data,
            'gameChoice': game.allGame
        }
        return render(request, 'custom/slideoverConfig/sub/update.html', content)

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

        GameSlideOverModel.objects.filter(id=int(id)).update(index=index,
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

        GameSlideOverModel.objects.filter(id=int(id)).delete()
        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleDelAll(cls, request):
        res = {}
        idstring = request.GET.get('data').encode("utf-8")
        if idstring:
            GameSlideOverModel.objects.extra(where=['id IN (' + idstring + ')']).delete()
            res['code'] = 1
        else:
            res['code'] = 0
            res['msg'] = '请选择有效值'

        return HttpResponse(json.dumps(res))

    @classmethod
    def handleCopy(cls, request):
        id = request.GET['id'].encode("utf-8")
        # 获取子表数据
        obj = GameSlideOverModel.objects.get(id=int(id))
        obj.id = None
        obj.save()
        return HttpResponse(json.dumps({
            "code": 1
        }))


