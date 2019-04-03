# -*- coding: utf-8 -*-

SOCKET_URL = (
    (0, '富豪服务器'),
    (1, '三消服务器'),
)

# 以飞刀对战为分界线， 飞刀对战（包括飞刀对战）以上为内部游戏，飞刀对战以下为外部游戏！！！！
WXAPPID_CHOICES = (
    # 祖玛工作室游戏放在当前行之下
    ("wxb7cb93eb49278934", "疯狂割草"),
    ("wx81319a080b7919e2", "旅行小西瓜"),
    ("wx81df03575e1e351f", "祖玛弹球"),
    ("wxaa5c62c26ee49681", "疯狂枪手"),
    ("wxbfebdafc2fc60b54", "富豪斗地主"),
    ("wxbb777fbea1e15f52", "新俄罗斯2048"),
    ("wx799e9a8af511be76", "最强小兔跑酷经典版"),
    ("wxb1d95fb6ebaf04eb", "十字消消消"),
    ("wx9f3847ace08e2ef0", "2048合并"),
    ("wx57f49f44206958e6", "欢乐钓鱼大师"),
    ("wxf1e6cc8e12d25d1f", "2048卡牌接龙"),
    ("wx6a9fc3d2c62410d8", "天天狙击"),
    ("wx824d94ce511885ad", "双枪王者"),
    ("wxb082d51f37021fac", "数字消消乐2"),
    ("wxe28531ea9f8164dc", "欢乐挖矿大师"),
    ("wx3e051a032d2386e9", "碰撞球球"),
    ("wxc1b648fc2fbc7ce8", "单机斗地主"),
    ("wx160e205dd45116c4", "球球大消除"),
    ("wxde9361a6865997fc", "3D球球打砖块"),
    ("wxd7062438a8b82506", "疯狂斧头"),
    ("wx352edabae2ef7a26", "合到8"),
    ("wxca71cd422b7fa67c", "合并三国"),
    ("wxa3855d93c407a5b6", "欢乐切水果大师"),
    ("wx950f5176e1d4ea9c", "欢乐射击大师"),
    ("wx234bfd171f00b4fc", "3D涂色迷宫"),
    ("wx7a2ecd52309f2466", "俄罗斯方块消除传奇"),
    ("wx2ff277bf28f5b970", "飞刀对战"),

    # 外部游戏放在当前行之下
    ("wx1668490543c6bae9", "天天游乐场"),
    ("wx785e80cff6120de5", "途游斗地主"),
    ("wx79ade44c39cefc7f", "传奇来了"),
    ("wxe11c116fc919cca1", "世界争霸"),
    ("wx45e02fc734c7b568", "俄罗斯方块拼图"),
    ("wxe46bd15fcbb4f829", "欢乐途游麻将"),
    ("wx30efe34580243475", "途游休闲捕鱼"),
    ("wxa9b801abd43333d9", "途游四川麻将"),
    ("wx4806f332084cae85", "途游捕鱼"),
    ("wx7cc3368d8ea0ed18", "3D战警"),
    ("wx85e9ff1a243bd54c", "西部射杀"),
    ("wx656cf75188e899bf", "王国无敌"),
    ("wxe20385ecec37a61d", "搭木板"),
    ("wxd9dac6412c7dab7b", "欢乐加1"),
    ("wx9bb2c795e0a6cc26", "数字三消"),
    ("wxb92d4d650d51eda8", "2048六角消除"),
    ("wx9b028af0bedc1ea7", "星星萌翻天"),
    ("wx38ba6e1a02228283", "玩爆2048"),
    ("wx760b441f8a68d7c6", "枪手来了"),
    ("wx148b43768fd2f0c8", "球球飞车"),
    ("wx30b605819c95270b", "战神录"),
    ("wx7243aa518129131d", "沙城战神"),
    ("wx6ae9fecf13de0423", "左右冲鸭"),
    ("wxd82849dc23eb4ac0", "挪车大师"),
    ("wxdb030d1934b15d67", "数字泡泡"),
    ("wx4b05395b61fd2aaf", "途游游戏"),
)

def wxappid_init():
    all_config = {}
    own_config = {}
    own_choice = ()
    iflag = 0
    for i in WXAPPID_CHOICES:
        all_config[i[0]] = i[1]
        if iflag == 1:
            continue
        own_config[i[0]] = i[1]
        own_choice = own_choice + ((i[0], i[1]),)
        if i[0] == 'wx2ff277bf28f5b970':
            iflag = 1

    return all_config, own_config, own_choice

WXAPPID_CONFIG, OWN_WXAPPID_CONFIG, OWN_WXAPPID_CHOICE = wxappid_init()

SANXIAO_SOCKET_URL_TEST = 'http://192.168.20.140:8000/'
SANXIAO_SOCKET_URL_FZ = 'https://xyxsxfz.nalrer.cn/'
SANXIAO_SOCKET_URL_ONLINE = 'https://xyxsx.nalrer.cn/'

FUHAO_SOCKET_URL_TEST = 'http://192.168.20.108:8000/'
FUHAO_SOCKET_URL_FZ = 'https://fz.nalrer.cn/'
FUHAO_SOCKET_URL_ONLINE = 'https://openrich.nalrer.cn/'


def getSocketUrl(id):
    if id == 0:
        return [FUHAO_SOCKET_URL_FZ, FUHAO_SOCKET_URL_ONLINE]
    elif id == 1:
        return [SANXIAO_SOCKET_URL_FZ, SANXIAO_SOCKET_URL_ONLINE]
    else:
        return []


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