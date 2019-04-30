# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render

from common import config
from gameInfo.game import allGame
from .models import *
from oriented.views import ORIENTED_TYPE, ORIENTED_TYPE_MODEL
from django.http import HttpResponse
from oriented.models import *
from gameInfo.models import GameInfoModel
from gameInfo.views import SOCKET_URL

class UpView(object):
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
        gameInfoObj = GameInfoModel.objects.get(wxAppid=appid)
        resData = []
        allData = uploadModel.objects.filter(game_id=gameInfoObj.game_id)
        for _temp in allData:
            _node = {
                'id': _temp.id,
                'name': allGame.get(_temp.name, ''),
                'wxAppId': appid,
                'socketUrl': SOCKET_URL.get(str(_temp.socket_url), ''),
                'orientedType': ORIENTED_TYPE.get(str(_temp.oriented_type), ''),
                'gameId': _temp.game_id,
                'status': '已加载' if _temp.status else '未加载',
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
        return render(request, 'upload/up/list.html')

    @classmethod
    def handleAdd(cls, request):
        appid = request.GET['appid'].encode("utf-8")
        content = {
            'appid': appid,
            'orientedType': ORIENTED_TYPE,
        }
        return render(request, 'upload/up/add.html', content)

    @classmethod
    def handleSave(cls, request):
        appid = request.POST['appid']
        oriented_type = request.POST['oriented_type']
        myFile = request.FILES['myFile']

        gameObj = GameInfoModel.objects.get(wxAppid=appid)

        uploadObj = uploadModel()
        uploadObj.oriented_type = int(oriented_type)
        uploadObj.socket_url = gameObj.socket_url
        uploadObj.game_id = gameObj.game_id
        uploadObj.name = appid
        uploadObj.file = myFile
        uploadObj.status = 0
        uploadObj.save()
        return HttpResponse(json.dumps({'info': '成功'}, ensure_ascii=False, separators=(',', ':')),
                            content_type="application/json,charset=utf-8")
    @classmethod
    def handleLook(cls, request):
        id = request.GET.get('id')
        basic_data = uploadModel.objects.filter(id=int(id))
        content = {
            'data': basic_data,
            'orientedType': ORIENTED_TYPE,
        }
        return render(request, 'upload/up/update.html', content)

    @classmethod
    def handleUpdate(cls, request):
        id = request.POST.get('id').encode("utf-8")
        oriented_type = request.POST['oriented_type']
        myFile = request.FILES['myFile']
        uploadModel.objects.filter(id=int(id)).update(oriented_type=oriented_type,
                                                      file=myFile)

        return HttpResponse(json.dumps({'info': '成功'}, ensure_ascii=False, separators=(',', ':')),
                            content_type="application/json,charset=utf-8")

    @classmethod
    def handleDel(cls, request):
        id = request.GET.get('id').encode("utf-8")
        uploadModel.objects.filter(id=int(id)).delete()

        return HttpResponse(json.dumps({
            "code": 1
        }))

    @classmethod
    def handleDelAll(cls, request):
        res = {}
        idstring = request.GET.get('data').encode("utf-8")
        if idstring:
            uploadModel.objects.extra(where=['id IN (' + idstring + ')']).delete()
            res['code'] = 1
        else:
            res['code'] = 0
            res['msg'] = '请选择有效值'

        return HttpResponse(json.dumps(res))

    @classmethod
    def handleLookInfo(cls, request):
        id = request.GET.get('id').encode("utf-8")
        upObj = uploadModel.objects.get(id=id)
        upObj.file.open()
        json_datas = upObj.file.read().decode("utf-8-sig")
        upObj.file.close()
        res = json.loads(json_datas, encoding='utf-8')
        return HttpResponse(json.dumps(res, indent=4, ensure_ascii=False, separators=(',', ':')),
                            content_type="application/json,charset=utf-8")

    @classmethod
    def handleLoadData(cls, request):
        appid = request.GET['appid'].encode("utf-8")
        if len(appid) == 18:
            pass
        else:
            config.flash(request, "提示", "请先选择游戏或检查当前游戏wxAppId正确性")
            return render(request, 'message.html')
        page = request.GET['page'].encode("utf-8")
        limit = request.GET['limit'].encode("utf-8")
        upLoadDatas = uploadModel.objects.filter(name=appid)
        resData = []
        for _temp in upLoadDatas:
            if _temp.status:
                continue
            _node = {
                'id': _temp.id,
                'name': allGame.get(_temp.name, ''),
                'wxAppId': appid,
                'socketUrl': SOCKET_URL.get(str(_temp.socket_url), ''),
                'orientedType': ORIENTED_TYPE.get(str(_temp.oriented_type), ''),
                'gameId': _temp.game_id,
                'status': '已加载' if _temp.status else '未加载',
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
    def handleLoadList(cls, request):
        return render(request, 'upload/load/list.html')

    @classmethod
    def handleLoad(cls, request):
        upload_id = request.GET.get('id').encode("utf-8")
        ret = False
        content = {}
        try:
            upload_datas = uploadModel.objects.get(id=upload_id)
            print upload_datas.status
            if not upload_datas.status:
                gameId = upload_datas.game_id
                wxappId = upload_datas.name
                oriented = upload_datas.oriented_type
                socket = upload_datas.socket_url

                upload_datas.file.open()
                json_datas = upload_datas.file.read().decode("utf-8-sig")
                upload_datas.file.close()
                temp_datas = json.loads(json_datas, encoding='utf-8')
                ret = handle_oriented_upload(gameId, wxappId, oriented, socket, temp_datas)
                if ret:
                    upload_datas.status = 1
                    upload_datas.save()
        except Exception, e:
            content['error'] = '失败! %s' % e
        content['info'] = ret
        return HttpResponse(json.dumps(content, indent=4, ensure_ascii=False, separators=(',', ':')),
                            content_type="application/json,charset=utf-8")


def handle_oriented_upload(gameId, wxappId, oriented_type, socket, upload_datas):
    oriented_model = ORIENTED_TYPE_MODEL.get(oriented_type)
    func = UPLOAD_ORIENTED.get(oriented_type)
    if func:
        return func(gameId, wxappId, oriented_model, socket, upload_datas)
    return False


def upload_oriented_IconSwitch(gameId, wxappId, oriented_model, socket, upload_datas):
    obj = oriented_model()
    obj.game_id = gameId
    obj.name = wxappId
    obj.socket_url = socket
    obj.switch = upload_datas['switch']
    obj.framesInterval = upload_datas['framesInterval']
    obj.user = 'import'
    obj.save()
    for _position in upload_datas['position']:
        posi_obj = PositionModel(foreignkey_iconswitch=obj)
        posi_obj.x = _position['x']
        posi_obj.y = _position['y']
        posi_obj.type = _position['type']
        posi_obj.position_id = _position['id']
        posi_obj.save()

    for _icon in upload_datas['icons']:
        icon_obj = GameIconSwitchModel(foreignkey_iconswitch=obj)
        icon_obj.wxAppId = _icon['openData'][0]['imgurl']
        icon_obj.weight = _icon['weight']
        icon_obj.scale = _icon['scale']
        icon_obj.imgLink = _icon['imgLink']
        icon_obj.openType = _icon['openType']
        icon_obj.clickHide = _icon['openData'][0]['clickHide']
        icon_obj.topath = _icon['topath']
        icon_obj.bi_iconId = _icon['biparam'][0]
        icon_obj.bi_educe_game = _icon['biparam'][4]
        icon_obj.bi_landing_page_id = _icon['biparam'][5]
        icon_obj.bi_landing_page = _icon['biparam'][2]
        icon_obj.save()
    return True


def upload_oriented_Strip(gameId, wxappId, oriented_model, socket, upload_datas):
    obj = oriented_model()
    obj.game_id = gameId
    obj.name = wxappId
    obj.socket_url = socket
    obj.label = upload_datas['label']
    obj.bg = upload_datas['bg']
    obj.reddot = upload_datas['reddot']
    obj.spacingX = upload_datas['spacingX']
    obj.iconWidth = upload_datas['iconWidth']
    obj.iconHeight = upload_datas['iconHeight']
    obj.switch = upload_datas['switch']
    obj.viewAdCounts = upload_datas['viewAdCounts']
    obj.framesInterval = upload_datas['framesInterval']
    obj.user = 'import'
    obj.save()

    for _icon in upload_datas['icons']:
        icon_obj = GameStripModel(foreignkey_strip=obj)
        icon_obj.index = _icon['index']
        icon_obj.wxAppId = _icon['openUrl']
        icon_obj.imgLink = _icon['imgLink']
        icon_obj.topath = _icon['topath']
        icon_obj.isClickHide = _icon.get('isClickHide', 0)
        icon_obj.bi_iconId = _icon['biparam'][0]
        icon_obj.bi_educe_game = _icon['biparam'][4]
        icon_obj.bi_landing_page_id = _icon['biparam'][5]
        icon_obj.bi_landing_page = _icon['biparam'][2]
        icon_obj.save()
    return True

def upload_oriented_SlideOver(gameId, wxappId, oriented_model, socket, upload_datas):
    obj = oriented_model()
    obj.game_id = gameId
    obj.name = wxappId
    obj.socket_url = socket
    obj.switch = upload_datas['switch']
    obj.fromWhere = upload_datas['fromWhere']
    obj.reddot = upload_datas['reddot']
    obj.mask = upload_datas['mask']
    obj.viewAdCounts = upload_datas['viewAdCounts']
    obj.user = 'import'
    obj.save()

    bg_obj = BgSlideOverModel(foreignkey_labelSlideOver=obj)
    bg_obj.bt_height = upload_datas['label']['height']
    bg_obj.bt_scale = upload_datas['label']['scale']
    bg_obj.bt_yfromtop = upload_datas['label']['yfromtop']
    bg_obj.bt_imgurl = upload_datas['label']['imgurl']

    bg_obj.kuang_positionY = upload_datas['bg']['positionY']
    bg_obj.kuang_bottomBlkHeight = upload_datas['bg']['bottomBlkHeight']
    bg_obj.kuang_imgurl = upload_datas['bg']['imgurl']

    bg_obj.la_scale = upload_datas['pull']['scale']
    bg_obj.la_positionX = upload_datas['pull']['positionX']
    bg_obj.la_positionY = upload_datas['pull']['positionY']
    bg_obj.la_imgurl0 = upload_datas['pull']['imgurl0']
    bg_obj.la_imgurl1 = upload_datas['pull']['imgurl1']
    bg_obj.la_isredon = upload_datas['pull']['isredon']

    bg_obj.icon_iconsWidth = upload_datas['grid']['iconsWidth']
    bg_obj.icon_iconsHeight = upload_datas['grid']['iconsHeight']
    bg_obj.icon_spacingX = upload_datas['grid']['spacingX']
    bg_obj.icon_spacingY = upload_datas['grid']['spacingY']
    bg_obj.icon_paddingLeft = upload_datas['grid']['paddingLeft']
    bg_obj.icon_paddingRight = upload_datas['grid']['paddingRight']

    bg_obj.text_size = upload_datas['text']['size']
    bg_obj.text_yfromIcon = upload_datas['text']['yfromIcon']
    bg_obj.text_colorR = upload_datas['text']['color'][0]
    bg_obj.text_colorG = upload_datas['text']['color'][1]
    bg_obj.text_colorB = upload_datas['text']['color'][2]

    bg_obj.save()

    for _icon in upload_datas['icons']:
        icon_obj = GameSlideOverModel(foreignkey_labelSlideOver=obj)
        icon_obj.index = _icon['index']
        icon_obj.text = _icon['text']
        icon_obj.type = _icon['type']
        icon_obj.imgLink = _icon['imgLink']
        icon_obj.openType = _icon['openType']
        icon_obj.openUrl = _icon['openUrl']
        icon_obj.isredon = _icon['isredon']
        icon_obj.topath = _icon['topath']
        icon_obj.bi_iconId = _icon['biparam'][0]
        icon_obj.bi_educe_game = _icon['biparam'][4]
        icon_obj.bi_landing_page_id = _icon['biparam'][5]
        icon_obj.bi_landing_page = _icon['biparam'][2]
        icon_obj.save()
    return True

def upload_oriented_end(gameId, wxappId, oriented_model, socket, upload_datas):
    obj = oriented_model()
    obj.game_id = gameId
    obj.name = wxappId
    obj.socket_url = socket
    obj.switch = upload_datas['switch']
    obj.reddot = upload_datas['reddot']
    obj.viewAdCounts = upload_datas['viewAdCounts']
    obj.user = 'import'
    obj.save()

    bg_obj = BgEndModel(foreignkey_EndModel=obj)
    bg_obj.label_height = upload_datas['label']['height']
    bg_obj.label_scale = upload_datas['label']['scale']
    bg_obj.label_yfromtop = upload_datas['label']['yfromtop']
    bg_obj.label_imgurl = upload_datas['label']['imgurl']

    bg_obj.bg_width = upload_datas['bg']['width']
    bg_obj.bg_height = upload_datas['bg']['height']
    bg_obj.bg_positionY = upload_datas['bg']['positionY']
    bg_obj.bg_imgurl = upload_datas['bg']['imgurl']

    bg_obj.grid_iconsWidth = upload_datas['grid']['iconsWidth']
    bg_obj.grid_iconsHeight = upload_datas['grid']['iconsHeight']
    bg_obj.save()

    for _icon in upload_datas['icons']:
        icon_obj = GameEndModel(foreignkey_EndModel=obj)
        icon_obj.index = _icon['index']
        icon_obj.text = _icon['text']
        icon_obj.type = _icon['type']
        icon_obj.imgLink = _icon['imgLink']
        icon_obj.openType = _icon['openType']
        icon_obj.openUrl = _icon['openUrl']
        icon_obj.isredon = _icon['isredon']
        icon_obj.topath = _icon['topath']
        icon_obj.bi_iconId = _icon['biparam'][0]
        icon_obj.bi_educe_game = _icon['biparam'][4]
        icon_obj.bi_landing_page_id = _icon['biparam'][5]
        icon_obj.bi_landing_page = _icon['biparam'][2]
        icon_obj.save()
    return True

UPLOAD_ORIENTED = {
    '0': upload_oriented_IconSwitch,
    '1': upload_oriented_Strip,
    '2': upload_oriented_SlideOver,
    '3': upload_oriented_end,
}
