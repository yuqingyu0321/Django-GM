# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render, HttpResponse, render_to_response
from .models import *
from common.config import WXAPPID_CONFIG


def get_curr_oriented(basic_id, type):
    return ORIENTED_TYPE_MODEL[type].objects.filter(id=int(basic_id))


def get_all_oriented(type):
    return ORIENTED_TYPE_MODEL[type].objects.all()


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
    obj_all_game = GameStripModel.objects.filter(foreignkey_strip_id=int(basic_id))
    for obj_game in obj_all_game:
        temp_dict = {}
        temp_dict['index'] = int(obj_game.index)
        temp_dict['imgLink'] = str(obj_game.imgLink)
        temp_dict['openUrl'] = str(obj_game.wxAppId)
        temp_dict['isClickHide'] = int(obj_game.isClickHide)
        temp_dict['topath'] = str(obj_game.topath)

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
    return response


def get_strip_educe_name(basic_ID):
    allName = ''
    obj_all_game = GameStripModel.objects.filter(foreignkey_strip_id=int(basic_ID))
    for obj_game in obj_all_game:
        wxAppId = str(obj_game.wxAppId)
        allName += WXAPPID_CONFIG.get(wxAppId, '')
        allName += '；'

    return allName[:-1] if allName else allName


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
        temp_dict['x'] = int(obj_position.x)
        temp_dict['y'] = int(obj_position.y)
        position.append(temp_dict)
    response['position'] = position

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
    return response


def get_iconswitch_name(basic_ID):
    allName = ''
    obj_all_game = GameIconSwitchModel.objects.filter(foreignkey_iconswitch=int(basic_ID))
    for obj_game in obj_all_game:
        wxAppId = str(obj_game.wxAppId)
        allName += WXAPPID_CONFIG.get(wxAppId, '')
        allName += '；'

    return allName[:-1] if allName else allName


def get_all_SlideOver_data(basic_id):
    response = {}

    obj_slideover = SlideOverModel.objects.filter(id=int(basic_id))
    response['switch'] = obj_slideover[0].switch
    response['fromWhere'] = obj_slideover[0].fromWhere
    response['reddot'] = obj_slideover[0].reddot
    response['mask'] = obj_slideover[0].mask
    response['viewAdCounts'] = obj_slideover[0].viewAdCounts

    label = {}
    obj_label = LabelSlideOverModel.objects.filter(foreignkey_labelSlideOver=int(basic_id))
    label['height'] = int(obj_label[0].height)
    label['scale'] = float(obj_label[0].scale)
    label['yfromtop'] = int(obj_label[0].yfromtop)
    label['imgurl'] = str(obj_label[0].imgurl)
    response['label'] = label

    pull = {}
    obj_pull = PullSlideOverModel.objects.filter(foreignkey_labelSlideOver=int(basic_id))
    pull['scale'] = float(obj_pull[0].scale)
    pull['positionX'] = int(obj_pull[0].positionX)
    pull['positionY'] = float(obj_pull[0].positionY)
    pull['imgurl0'] = str(obj_pull[0].imgurl0)
    pull['imgurl1'] = str(obj_pull[0].imgurl1)
    pull['isredon'] = int(obj_pull[0].isredon)
    response['pull'] = pull

    bg = {}
    obj_bg = BgSlideOverModel.objects.filter(foreignkey_labelSlideOver=int(basic_id))
    bg['positionY'] = float(obj_bg[0].positionY)
    bg['bottomBlkHeight'] = int(obj_bg[0].bottomBlkHeight)
    bg['imgurl'] = str(obj_bg[0].imgurl)
    response['bg'] = bg

    grid = {}
    obj_grid = GridSlideOverModel.objects.filter(foreignkey_labelSlideOver=int(basic_id))
    grid['iconsWidth'] = int(obj_grid[0].iconsWidth)
    grid['iconsHeight'] = int(obj_grid[0].iconsHeight)
    grid['spacingX'] = int(obj_grid[0].spacingX)
    grid['spacingY'] = int(obj_grid[0].spacingY)
    grid['paddingLeft'] = int(obj_grid[0].paddingLeft)
    grid['paddingRight'] = int(obj_grid[0].paddingRight)
    response['grid'] = grid

    text = {}
    obj_text = TextSlideOverModel.objects.filter(id=int(basic_id))
    text['size'] = int(obj_text[0].size)
    text['yfromIcon'] = int(obj_text[0].yfromIcon)
    text['color'] = [
        int(obj_text[0].colorR), int(obj_text[0].colorG), int(obj_text[0].colorB)
    ]
    response['text'] = text

    icon = []
    obj_all_game = GameSlideOverModel.objects.filter(foreignkey_labelSlideOver=int(basic_id))
    for obj_game in obj_all_game:
        temp_dict = {}
        temp_dict['index'] = int(obj_game.index)
        temp_dict['text'] = str(obj_game.text)
        temp_dict['type'] = int(obj_game.type)
        temp_dict['imgLink'] = str(obj_game.imgLink)
        temp_dict['openUrl'] = str(obj_game.openUrl)
        temp_dict['isredon'] = int(obj_game.isredon)
        temp_dict['topath'] = str(obj_game.topath)

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
    return response


def get_slideover_educe_name(basic_ID):
    allName = ''
    obj_all_game = GameSlideOverModel.objects.filter(foreignkey_labelSlideOver=int(basic_ID))
    for obj_game in obj_all_game:
        wxAppId = str(obj_game.openUrl)
        allName += WXAPPID_CONFIG.get(wxAppId, '')
        allName += '；'

    return allName[:-1] if allName else allName


ORIENTED_TYPE_MODEL = {
    '0': IconSwitchModel,
    '1': StripModel,
    '2': SlideOverModel,
}

ORIENTED_TYPE = {
    '0': 'icon切换',
    '1': '导流条',
    '2': '侧拉框',
}

ORIENTED_TYPE_GET_ALL_FUNC = {
    '0': get_all_iconswitch_data,
    '1': get_all_gameStrip_data,
    '2': get_all_SlideOver_data,
}

ORIENTED_TYPE_GET_EDUCENAME_FUNC = {
    '0': get_iconswitch_name,
    '1': get_strip_educe_name,
    '2': get_slideover_educe_name,
}

ORIENTED_TYPE_SERVER_ID = {
    '0': 'iconSwitch',
    '1': 'strip',
    '2': 'slideOver',
}
