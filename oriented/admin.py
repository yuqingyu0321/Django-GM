# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from common.config import OWN_WXAPPID_CONFIG
from django.contrib import admin
from .models import *
from django import forms
from .views import *


class GameStripInline(admin.StackedInline):
    model = GameStripModel
    extra = 0
    max_num = 10


class StripForm(forms.ModelForm):
    class Meta:
        widgets = {
            # 'code': TextInput(attrs={'class': 'input-mini'}),
            # 'independence_day': SuitDateWidget,
            #'description': AutosizedTextarea,
            #'architecture': AutosizedTextarea,
            #'continent': LinkedSelect,
        }

@admin.register(StripModel)
class StripAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = [ 'id', 'game_name', 'educe_game', 'user', 'create_time', 'modifi_time']
    list_display_links = ['game_name']
    # 内联
    inlines = [
        GameStripInline,
    ]
    form = StripForm
    list_per_page = 50

    save_as = True
    search_fields = ('name',)

    def game_name(self, obj):
        return OWN_WXAPPID_CONFIG.get(obj.name, '')
    game_name.short_description = '游戏名称'

    def educe_game(self, obj):
        return get_strip_educe_name(obj.id)
    educe_game.short_description = '导出游戏'

    def save_model(self, request, obj, form, change):
        obj.user = request.user.username
        super(StripAdmin, self).save_model(request, obj, form, change)

# admin.site.register(Oriented, OrientedAdmin)


class GameIconSwitchModelInline(admin.StackedInline):
    model = GameIconSwitchModel
    extra = 0
    max_num = 10


class PositionModelInline(admin.TabularInline):
    model = PositionModel
    extra = 0

@admin.register(IconSwitchModel)
class IconSwitchModelAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ['id', 'game_name', 'educe_game', 'user', 'create_time', 'modifi_time']
    list_display_links = ['game_name']
    # 内联
    inlines = [
        PositionModelInline,
        GameIconSwitchModelInline,
    ]
    list_per_page = 50

    save_as = True
    search_fields = ('name',)

    def game_name(self, obj):
        return OWN_WXAPPID_CONFIG.get(obj.name, '')
    game_name.short_description = '游戏名称'

    def educe_game(self, obj):
        return get_iconswitch_name(obj.id)
    educe_game.short_description = '导出游戏'

    def save_model(self, request, obj, form, change):
        obj.user = request.user.username
        super(IconSwitchModelAdmin, self).save_model(request, obj, form, change)


class GameSlideOverModelInline(admin.StackedInline):
    model = GameSlideOverModel
    extra = 0
    max_num = 10

class TextSlideOverModelInline(admin.TabularInline):
    model = TextSlideOverModel
    extra = 1
    min_num = 1
    max_num = 1

class GridSlideOverModelInline(admin.TabularInline):
    model = GridSlideOverModel
    extra = 1
    min_num = 1
    max_num = 1

class BgSlideOverModelInline(admin.TabularInline):
    model = BgSlideOverModel
    extra = 1
    min_num = 1
    max_num = 1

class PullSlideOverModelInline(admin.TabularInline):
    model = PullSlideOverModel
    extra = 1
    min_num = 1
    max_num = 1

class LabelSlideOverModelInline(admin.TabularInline):
    model = LabelSlideOverModel
    extra = 1
    min_num = 1
    max_num = 1

@admin.register(SlideOverModel)
class SlideOverModelAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = [ 'id', 'game_name', 'educe_game', 'user', 'create_time', 'modifi_time']
    list_display_links = ['game_name']
    # 内联
    inlines = [
        LabelSlideOverModelInline,
        PullSlideOverModelInline,
        BgSlideOverModelInline,
        GridSlideOverModelInline,
        TextSlideOverModelInline,
        GameSlideOverModelInline,
    ]
    list_per_page = 50

    save_as = True
    search_fields = ('name',)

    def game_name(self, obj):
        return OWN_WXAPPID_CONFIG.get(obj.name, '')
    game_name.short_description = '游戏名称'

    def educe_game(self, obj):
        return get_slideover_educe_name(obj.id)
    educe_game.short_description = '导出游戏'

    def save_model(self, request, obj, form, change):
        obj.user = request.user.username
        super(SlideOverModelAdmin, self).save_model(request, obj, form, change)