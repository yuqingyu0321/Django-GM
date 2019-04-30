# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from gameInfo.game import allGame
from .models import *


def get_curr_oriented(basic_id, type):
    return ORIENTED_TYPE_MODEL[type].objects.filter(id=int(basic_id))


def get_all_oriented(type):
    return ORIENTED_TYPE_MODEL[type].objects.all().order_by('-id')


def get_wxAppId_oriented(type, wxApppId):
    return ORIENTED_TYPE_MODEL[type].objects.filter(name=wxApppId).order_by('-id')


def get_all_gameStrip_data(basic_id):
    response = {}

    obj_strip = StripModel.objects.filter(id=int(basic_id))
    response['switch'] = obj_strip[0].switch
    response['label'] = obj_strip[0].label
    response['bg'] = obj_strip[0].bg
    response['reddot'] = obj_strip[0].reddot
    response['spacingX'] = obj_strip[0].spacingX
    response['iconWidth'] = obj_strip[0].iconWidth
    response['iconHeight'] = obj_strip[0].iconHeight
    response['viewAdCounts'] = obj_strip[0].viewAdCounts
    response['framesInterval'] = obj_strip[0].framesInterval

    icon = []
    wxAppIdList = []
    obj_all_game = GameStripModel.objects.filter(foreignkey_strip_id=int(basic_id))
    for obj_game in obj_all_game:
        temp_dict = {}
        temp_dict['index'] = int(obj_game.index)
        temp_dict['imgLink'] = str(obj_game.imgLink)
        temp_dict['openUrl'] = str(obj_game.wxAppId)
        temp_dict['isClickHide'] = int(obj_game.isClickHide)
        temp_dict['topath'] = str(obj_game.topath)
        wxAppIdList.append(obj_game.wxAppId)

        biParam = []
        biParam.append(str(obj_game.bi_iconId))
        biParam.append('{}{}'.format(obj_game.bi_iconId, obj_game.bi_landing_page_id))
        biParam.append(obj_game.bi_landing_page)
        biParam.append(str(obj_game.wxAppId))
        biParam.append(obj_game.bi_educe_game)
        biParam.append(obj_game.bi_landing_page_id)
        biParam.append(1)
        temp_dict['biparam'] = biParam

        icon.append(temp_dict)

    response['icons'] = icon
    return response, wxAppIdList


def get_strip_educe_name(basic_ID):
    allName = []
    obj_all_game = GameStripModel.objects.filter(foreignkey_strip_id=int(basic_ID))
    for obj_game in obj_all_game:
        wxAppId = str(obj_game.wxAppId)
        name = allGame.get(wxAppId, '')
        allName.append(name)

    return allName


def get_all_iconswitch_data(basic_id):
    response = {}

    obj_strip = IconSwitchModel.objects.filter(id=int(basic_id))
    response['switch'] = obj_strip[0].switch
    response['framesInterval'] = obj_strip[0].framesInterval

    position = []
    obj_all_position = PositionModel.objects.filter(foreignkey_iconswitch=int(basic_id))
    for obj_position in obj_all_position:
        temp_dict = {}
        temp_dict['id'] = int(obj_position.position_id)
        temp_dict['type'] = int(obj_position.type)
        temp_dict['x'] = obj_position.x
        temp_dict['y'] = obj_position.y
        position.append(temp_dict)
    response['position'] = position

    wxAppIdList = []
    icon = []
    obj_all_game = GameIconSwitchModel.objects.filter(foreignkey_iconswitch=int(basic_id))
    for obj_game in obj_all_game:
        temp_dict = {}
        temp_dict['weight'] = int(obj_game.weight)
        temp_dict['scale'] = float(obj_game.scale)
        temp_dict['imgLink'] = str(obj_game.imgLink)
        temp_dict['openType'] = int(obj_game.openType)
        temp_dict['openData'] = [{'clickHide': int(obj_game.clickHide), 'imgurl': str(obj_game.wxAppId)}]
        temp_dict['topath'] = str(obj_game.topath)
        wxAppIdList.append(obj_game.wxAppId)
        biParam = []
        biParam.append(str(obj_game.bi_iconId))
        biParam.append('{}{}'.format(obj_game.bi_iconId, obj_game.bi_landing_page_id))
        biParam.append(obj_game.bi_landing_page)
        biParam.append(str(obj_game.wxAppId))
        biParam.append(obj_game.bi_educe_game)
        biParam.append(obj_game.bi_landing_page_id)
        biParam.append(1)
        temp_dict['biparam'] = biParam

        icon.append(temp_dict)

    response['icons'] = icon
    return response, wxAppIdList


def get_iconswitch_name(basic_ID):
    allName = []
    obj_all_game = GameIconSwitchModel.objects.filter(foreignkey_iconswitch=int(basic_ID))
    for obj_game in obj_all_game:
        wxAppId = str(obj_game.wxAppId)
        name = allGame.get(wxAppId, '')
        allName.append(name)

    return allName


def get_all_SlideOver_data(basic_id):
    response = {}

    obj_slideover = SlideOverModel.objects.filter(id=int(basic_id))
    response['switch'] = obj_slideover[0].switch
    response['fromWhere'] = obj_slideover[0].fromWhere
    response['reddot'] = obj_slideover[0].reddot
    response['mask'] = obj_slideover[0].mask
    response['viewAdCounts'] = obj_slideover[0].viewAdCounts

    bg = {}
    obj_bg = BgSlideOverModel.objects.filter(foreignkey_labelSlideOver=int(basic_id))
    bg['positionY'] = float(obj_bg[0].kuang_positionY)
    bg['bottomBlkHeight'] = int(obj_bg[0].kuang_bottomBlkHeight)
    bg['imgurl'] = str(obj_bg[0].kuang_imgurl)
    response['bg'] = bg

    label = {}
    label['height'] = obj_bg[0].bt_height
    label['scale'] = obj_bg[0].bt_scale
    label['yfromtop'] = obj_bg[0].bt_yfromtop
    label['imgurl'] = obj_bg[0].bt_imgurl
    response['label'] = label

    pull = {}
    pull['scale'] = obj_bg[0].la_scale
    pull['positionX'] = obj_bg[0].la_positionX
    pull['positionY'] = obj_bg[0].la_positionY
    pull['imgurl0'] = obj_bg[0].la_imgurl0
    pull['imgurl1'] = obj_bg[0].la_imgurl1
    pull['isredon'] = 1 if obj_bg[0].la_isredon else 0
    response['pull'] = pull

    grid = {}
    grid['iconsWidth'] = obj_bg[0].icon_iconsWidth
    grid['iconsHeight'] = obj_bg[0].icon_iconsHeight
    grid['spacingX'] = obj_bg[0].icon_spacingX
    grid['spacingY'] = obj_bg[0].icon_spacingY
    grid['paddingLeft'] = obj_bg[0].icon_paddingLeft
    grid['paddingRight'] = obj_bg[0].icon_paddingRight
    response['grid'] = grid

    text = {}
    text['size'] = obj_bg[0].text_size
    text['yfromIcon'] = obj_bg[0].text_yfromIcon
    text['color'] = [
        obj_bg[0].text_colorR, obj_bg[0].text_colorG, obj_bg[0].text_colorB
    ]
    response['text'] = text

    icon = []
    wxAppIdList = []
    obj_all_game = GameSlideOverModel.objects.filter(foreignkey_labelSlideOver=int(basic_id))
    for obj_game in obj_all_game:
        temp_dict = {}
        temp_dict['index'] = int(obj_game.index)
        temp_dict['text'] = str(obj_game.text)
        temp_dict['type'] = int(obj_game.type)
        temp_dict['imgLink'] = str(obj_game.imgLink)
        temp_dict['openType'] = int(obj_game.openType)
        temp_dict['openUrl'] = str(obj_game.openUrl)
        temp_dict['isredon'] = int(obj_game.isredon)
        temp_dict['topath'] = str(obj_game.topath)
        wxAppIdList.append(obj_game.openUrl)

        biParam = []
        biParam.append(str(obj_game.bi_iconId))
        biParam.append('{}{}'.format(obj_game.bi_iconId, obj_game.bi_landing_page_id))
        biParam.append(obj_game.bi_landing_page)
        biParam.append(str(obj_game.openUrl))
        biParam.append(obj_game.bi_educe_game)
        biParam.append(obj_game.bi_landing_page_id)
        biParam.append(1)
        temp_dict['biparam'] = biParam

        icon.append(temp_dict)

    response['icons'] = icon
    return response, wxAppIdList


def get_slideover_educe_name(basic_ID):
    allName = []
    obj_all_game = GameSlideOverModel.objects.filter(foreignkey_labelSlideOver=int(basic_ID))
    for obj_game in obj_all_game:
        wxAppId = str(obj_game.openUrl)
        name = allGame.get(wxAppId, '')
        allName.append(name)

    return allName


def get_all_end_data(basic_id):
    response = {}

    obj_end = EndModel.objects.get(id=int(basic_id))

    response['switch'] = obj_end.switch
    response['reddot'] = obj_end.reddot
    response['viewAdCounts'] = obj_end.viewAdCounts

    obj_bg = BgEndModel.objects.filter(foreignkey_EndModel=int(basic_id))
    if obj_bg:
        label = {}
        label['height'] = obj_bg[0].label_height
        label['scale'] = obj_bg[0].label_scale
        label['yfromtop'] = obj_bg[0].label_yfromtop
        label['imgurl'] = obj_bg[0].label_imgurl
        response['label'] = label

        bg = {}
        bg['width'] = obj_bg[0].bg_width
        bg['height'] = obj_bg[0].bg_height
        bg['positionY'] = obj_bg[0].bg_positionY
        bg['imgurl'] = obj_bg[0].bg_imgurl
        response['bg'] = bg

        grid = {}
        grid['iconsWidth'] = obj_bg[0].grid_iconsWidth
        grid['iconsHeight'] = obj_bg[0].grid_iconsHeight
        response['grid'] = grid

    icon = []
    wxAppIdList = []
    obj_all_game = GameEndModel.objects.filter(foreignkey_EndModel=int(basic_id))
    for obj_game in obj_all_game:
        temp_dict = {}
        temp_dict['index'] = int(obj_game.index)
        temp_dict['text'] = str(obj_game.text)
        temp_dict['type'] = int(obj_game.type)
        temp_dict['imgLink'] = str(obj_game.imgLink)
        temp_dict['openType'] = int(obj_game.openType)
        temp_dict['openUrl'] = str(obj_game.openUrl)
        temp_dict['isredon'] = int(obj_game.isredon)
        temp_dict['topath'] = str(obj_game.topath)
        wxAppIdList.append(obj_game.openUrl)

        biParam = []
        biParam.append(str(obj_game.bi_iconId))
        biParam.append('{}{}'.format(obj_game.bi_iconId, obj_game.bi_landing_page_id))
        biParam.append(obj_game.bi_landing_page)
        biParam.append(str(obj_game.openUrl))
        biParam.append(obj_game.bi_educe_game)
        biParam.append(obj_game.bi_landing_page_id)
        biParam.append(1)
        temp_dict['biparam'] = biParam

        icon.append(temp_dict)

    response['icons'] = icon
    return response, wxAppIdList

def get_end_educe_name(basic_ID):
    allName = []
    obj_all_game = GameEndModel.objects.filter(foreignkey_EndModel=int(basic_ID))
    for obj_game in obj_all_game:
        wxAppId = str(obj_game.openUrl)
        name = allGame.get(wxAppId, '')
        allName.append(name)

    return allName

ORIENTED_TYPE_MODEL = {
    '0': IconSwitchModel,
    '1': StripModel,
    '2': SlideOverModel,
    '3': EndModel,
}

ORIENTED_TYPE = {
    '0': 'Icon切换',
    '1': '导流条',
    '2': '侧拉框',
    '3': '结束页',
}

ORIENTED_TYPE_GET_ALL_FUNC = {
    '0': get_all_iconswitch_data,
    '1': get_all_gameStrip_data,
    '2': get_all_SlideOver_data,
    '3': get_all_end_data,
}

ORIENTED_TYPE_GET_EDUCENAME_FUNC = {
    '0': get_iconswitch_name,
    '1': get_strip_educe_name,
    '2': get_slideover_educe_name,
    '3': get_end_educe_name,
}

ORIENTED_TYPE_SERVER_ID = {
    '0': 'iconSwitch',
    '1': 'strip',
    '2': 'slideOver',
    '3': 'end',
}


def handle_userAndTime(request, basicId, typeId, fz):
    if fz:
        return
    currOrientedQuery = ORIENTED_TYPE_MODEL[typeId].objects.get(id=int(basicId))
    currOrientedQuery.online_modifi_time = datetime.now()
    currOrientedQuery.online_user = request.user.username
    currOrientedQuery.save(update_fields=['online_modifi_time', 'online_user'])
