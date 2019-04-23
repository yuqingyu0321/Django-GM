# -*- coding: utf-8 -*-
from .models import *

innerGame = {}
inner2GameId = {}
externalGame = {}
allGame = {}
allGameId = {}

def _init():
    gameALl = GameInfoModel.objects.all()

    for temp in gameALl:
        if temp.inner_game:
            innerGame[temp.wxAppid] = temp.name
            inner2GameId[temp.wxAppid] = temp.game_id
        else:
            externalGame[temp.wxAppid] = temp.name
        allGame[temp.wxAppid] = temp.name
        allGameId[temp.wxAppid] = temp.game_id

    print '_init', innerGame, inner2GameId, externalGame, allGame, allGameId


def _removeGame(obj):
    if obj.inner_game:
        innerGame.pop(obj.wxAppid)
        inner2GameId.pop(obj.wxAppid)
    else:
        externalGame.pop(obj.wxAppid)
    allGameId.pop(obj.wxAppid)
    allGame.pop(obj.wxAppid)

    print '_removeGame', innerGame, inner2GameId, externalGame, allGame, allGameId

def _removeAllGame(objList):
    for temp in objList:
        if temp.inner_game:
            innerGame.pop(temp.wxAppid)
            inner2GameId.pop(temp.wxAppid)
        else:
            externalGame.pop(temp.wxAppid)
        allGameId.pop(temp.wxAppid)
        allGame.pop(temp.wxAppid)
    print '_removeAllGame', innerGame, inner2GameId, externalGame, allGame, allGameId

def _addGame(obj):
    if obj.inner_game:
        innerGame[obj.wxAppid] = obj.name
        inner2GameId[obj.wxAppid] = obj.game_id
    else:
        externalGame[obj.wxAppid] = obj.name

    allGame[obj.wxAppid] = obj.name
    allGameId[obj.wxAppid] = obj.game_id
    print '_addGame', innerGame, inner2GameId, externalGame, allGame, allGameId
