# -*- coding: utf-8 -*-

SOCKET_URL = (
    (0, '富豪服务器'),
    (1, '三消服务器'),
)

WXAPPID_CHOICES = (
    ('wxaa5c62c26ee49681', '疯狂枪手'),
    ('wx57f49f44206958e6', '欢乐钓鱼大师'),
    ('wxde9361a6865997fc', '3D球球打砖块'),
    # (20235, '俄罗斯方块消除传奇'),
    # (20037, '祖玛弹球'),
    # (6, '富豪斗地主'),
    # (20241, '欢乐水果大师'),
    # (20232, '疯狂斧头'),
    # ('9', '旅行小西瓜'),
    # ('10', '碰撞球球'),
    # (301, '新俄罗斯2048'),
    # (110, '天天狙击'),
    # (108, '数字消消乐2'),
    # (20081, '十字消消消'),
    # (127, '合到8'),
    # (128, '飞刀对战'),
)

WXAPPID_CONFIG = {
    'wxaa5c62c26ee49681': '疯狂枪手',
    'wx57f49f44206958e6': '钓鱼大师',
    'wxde9361a6865997fc': '3D球球打砖块',
}

SANXIAO_SOCKET_URL_FZ = 'https://xyxsxfz.nalrer.cn/'
SANXIAO_SOCKET_URL_ONLINE = 'https://xyxsx.nalrer.cn/'

FUHAO_SOCKET_URL_FZ = 'https://fz.nalrer.cn/'
FUHAO_SOCKET_URL_ONLINE = 'https://openrich.nalrer.cn/'

def getSocketUrl(id):
    if id == 0:
        return [FUHAO_SOCKET_URL_FZ, FUHAO_SOCKET_URL_ONLINE]
    elif id == 1:
        return ['http://192.168.20.140:8000/', SANXIAO_SOCKET_URL_ONLINE]
    else:
        return []



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


