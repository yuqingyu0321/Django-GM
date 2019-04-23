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


def get_all_uploadModel_data():
    return uploadModel.objects.all().order_by('-id')


def get_wxappId_uploadModel_data(wxAppId):
    return uploadModel.objects.filter(name=wxAppId).order_by('-id')


def get_use_dict():
    show_all = get_all_uploadModel_data()
    temp_data = show_all.filter(status=0)
    for i in temp_data:
        i.name = allGame.get(i.name, '')
        i.oriented_type = ORIENTED_TYPE.get(i.oriented_type, '')
        i.status = '已加载' if i.status else '未加载'
    content = {
        'uploadData': temp_data,
        'gameChoice': allGame,
    }

    return content


def show_upload(request):
    return render(request, 'upload/index.html', get_use_dict())


def show_game_upload(request):
    wxAppId = request.GET.get('search_wxAppId')
    if wxAppId:
        data = get_wxappId_uploadModel_data(wxAppId)
        for i in data:
            i.name = allGame.get(i.name, '')
            i.oriented_type = ORIENTED_TYPE.get(i.oriented_type, '')
            i.status = '已加载' if i.status else '未加载'
        content = {
            'uploadData': data,
            'gameChoice': allGame,
        }
    else:
        content = get_use_dict()

    return render(request, 'upload/index.html', content)


def upload_load(request, upload_id):
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


UPLOAD_ORIENTED = {
    '0': upload_oriented_IconSwitch,
    '1': upload_oriented_Strip,
    '2': upload_oriented_SlideOver,
}
