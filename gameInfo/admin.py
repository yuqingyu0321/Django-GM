# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


@admin.register(GameInfoModel)
class GameInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'wxAppid', 'inner_game')