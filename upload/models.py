# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import time
import uuid
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.conf import settings
from django.db import models
from common.config import SOCKET_URL
from gameInfo.game import allGame



def file_name(instance, filename):
    ext = filename.split('.')[-1]
    name = filename.split('.')[0]
    date_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    filename = '{}_{}_{}.{}'.format(name, date_time, uuid.uuid1().hex[:10], ext)
    return filename

class uploadModel(models.Model):

    ORIENTED_TYPE = (
        ('0', 'Icon切换'),
        ('1', '导流条'),
        ('2', '侧拉框'),
    )

    game_id = models.PositiveIntegerField(verbose_name='gameId')
    socket_url = models.PositiveIntegerField(verbose_name='服务器', choices=SOCKET_URL)
    name = models.CharField(verbose_name='游戏名称', max_length=255)
    oriented_type = models.CharField(verbose_name='导流类型', choices=ORIENTED_TYPE, max_length=255)
    status = models.BooleanField(verbose_name='文件状态', default=0, editable=False)
    file = models.FileField(upload_to=file_name, verbose_name='json文件')

    user = models.CharField(editable=False, null=True, verbose_name='操作人', max_length=255)

    def __str__(self):
        return allGame.get(self.name, '')

    class Meta:
        verbose_name = '文件上传'
        verbose_name_plural = verbose_name


@receiver(pre_delete, sender=uploadModel)
def uploadModel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.file.delete(False)

