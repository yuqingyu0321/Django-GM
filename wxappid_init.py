# -*- coding: utf-8 -*-

import os
from gameInfo.models import GameInfoModel

with open('allwxappid') as file_obj:
    for line in file_obj:
        c = line.split("\"")
        print c[1],c[2],c[3],c[4],c[5]

        obj = GameInfoModel()
        obj.name = c[1]
        obj.game_id = int(c[3])
        obj.wxAppid = c[2]
        obj.socket_url = int(c[4])
        obj.inner_game = int(c[5])
        obj.save()

