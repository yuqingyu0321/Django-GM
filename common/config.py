# -*- coding: utf-8 -*-

SOCKET_URL = (
    (0, '富豪服务器'),
    (1, '三消服务器'),
    (9999, '其他服务器'),
)

SANXIAO_SOCKET_URL_TEST = 'http://192.168.20.140:8000/'
SANXIAO_SOCKET_URL_FZ = 'https://xyxsxfz.nalrer.cn/'
SANXIAO_SOCKET_URL_ONLINE = 'https://xyxsx.nalrer.cn/'

FUHAO_SOCKET_URL_TEST = 'http://192.168.20.108:8000/'
FUHAO_SOCKET_URL_FZ = 'https://fz.nalrer.cn/'
FUHAO_SOCKET_URL_ONLINE = 'https://openrich.nalrer.cn/'


def getSocketUrl(id):
    if id == 0:
        return FUHAO_SOCKET_URL_TEST
    elif id == 1:
        return SANXIAO_SOCKET_URL_TEST
    else:
        return ''


def gain_SetSocketApi(id):
    if id == 0:
        return 'v3/game/zmgm/set'
    elif id == 1:
        return 'api/wx/zmgm/set'
    else:
        return ''

def gain_GetSocketApi(id):
    if id == 0:
        return 'v3/game/zmgm/get'
    elif id == 1:
        return 'api/wx/zmgm/get'
    else:
        return ''


from django.contrib import messages


def flash(request, title, text, level='info'):
    """
    利用django的message系统发送一个信息。
    """
    level_map = {
        'info': messages.INFO,
        'debug': messages.DEBUG,
        'success': messages.SUCCESS,
        'warning': messages.WARNING,
        'error': messages.ERROR
    }

    level = level_map[level]

    messages.add_message(request, level, text, extra_tags=title)
    return 'ok'

import time

def timeStampToStr(ts, formatTime = "%Y-%m-%d %H:%M:%S"):
    t = time.localtime(ts)
    return time.strftime(formatTime, t)