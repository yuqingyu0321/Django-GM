# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from gameInfo.game import allGame
from django.contrib import admin
from .models import *
from oriented.views import ORIENTED_TYPE

@admin.register(uploadModel)
class uploadModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'game_name', 'oriented', 'file', 'file_status', 'user']
    list_display_links = ['game_name']

    save_as = True
    search_fields = ('name',)
    ordering = ('-id',)

    def game_name(self, obj):
        return allGame.get(obj.name, '')
    game_name.short_description = '游戏名称'

    def oriented(self, obj):
        return ORIENTED_TYPE.get(obj.oriented_type, '')
    oriented.short_description = '导流类型'

    def file_status(self, obj):
        return '已加载' if obj.status else '未加载'
    file_status.short_description = '文件状态'

    def save_model(self, request, obj, form, change):
        obj.user = request.user.username
        super(uploadModelAdmin, self).save_model(request, obj, form, change)