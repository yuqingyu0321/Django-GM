# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from common.config import SOCKET_URL

class GameInfoModel(models.Model):
    game_id = models.PositiveIntegerField(verbose_name='gameId', default=0)
    name = models.CharField(verbose_name='游戏名称', max_length=255)
    wxAppid = models.CharField(verbose_name='WxAppId', max_length=21)
    socket_url = models.PositiveIntegerField(verbose_name='服务器', choices=SOCKET_URL)
    inner_game = models.BooleanField(verbose_name='内部游戏', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '游戏配置'
        verbose_name_plural = verbose_name
