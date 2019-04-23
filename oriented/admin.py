# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from gameInfo.game import allGame
from django.contrib import admin
from .models import *
from django import forms
from .views import *
from suit.widgets import EnclosedInput

class GameStripModelForm(forms.ModelForm):
    class Meta:
        widgets = {
            'imgLink': EnclosedInput(
                append='<button class="layui-btn layui-btn-xs"type="button" onclick="fun_imgLink(this)">预览</button><script language="javascript">\
                function fun_imgLink (obj){\
                    var x = obj.previousSibling;; window.open(x.value);}</script>',
            ),
            'bi_landing_page': EnclosedInput(
                append='<button class="layui-btn layui-btn-xs"type="button" onclick="fun_bi_landing_page(this)">预览</button><script language="javascript">\
                        function fun_bi_landing_page (obj){\
                            var x = obj.previousSibling;; window.open(x.value);}</script>',
            ),
        }

class GameStripInline(admin.StackedInline):
    model = GameStripModel
    extra = 0
    max_num = 10
    form = GameStripModelForm
    fieldsets = [
        (
            '▼',
            {
                'fields': [
                    'index',
                    ('wxAppId', 'topath'),
                    'imgLink',
                    'isClickHide',
                    'bi_iconId',
                    'bi_landing_page_id',
                    'bi_educe_game',
                    'bi_landing_page',
                ],
                'classes': [
                    'collapse'
                ]
            }
        )]

class StripForm(forms.ModelForm):
    class Meta:
        widgets = {
            'label': EnclosedInput(
                append='<button class="layui-btn layui-btn-xs" type="button" onclick="fun_label()">预览</button><script language="javascript">\
                function fun_label (){\
                    var x=document.getElementById("id_label");window.open(x.value);}</script>',
            ),
            'bg':EnclosedInput(
                append='<button class="layui-btn layui-btn-xs" type="button" onclick="fun_bg()">预览</button><script language="javascript">\
                function fun_bg (){\
                    var x=document.getElementById("id_bg");window.open(x.value);}</script>',
            ),
            'reddot':EnclosedInput(
                append='<button class="layui-btn layui-btn-xs" type="button" onclick="fun_reddot()">预览</button><script language="javascript">\
                function fun_reddot (){\
                    var x=document.getElementById("id_reddot");window.open(x.value);}</script>',
            ),
        }


@admin.register(StripModel)
class StripAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ['id', 'game_name', 'educe_game', 'user', 'create_time', 'modifi_time']
    list_display_links = ['game_name']
    # 内联
    inlines = [
        GameStripInline,
    ]
    fieldsets = [
        (
            None,
            {
                'fields': [
                    'name',
                    'game_id',
                    'socket_url',
                    ('spacingX', 'iconWidth', 'iconHeight'),
                    ('switch', 'viewAdCounts', 'framesInterval'),
                    'label',
                    'bg',
                    'reddot'
                ]
            }
        )]

    form = StripForm
    list_per_page = 50

    save_as = True
    search_fields = ('name',)
    ordering = ('-id',)

    def game_name(self, obj):
        return allGame.get(obj.name, '')

    game_name.short_description = '游戏名称'

    def educe_game(self, obj):
        return get_strip_educe_name(obj.id)

    educe_game.short_description = '导出游戏'

    def save_model(self, request, obj, form, change):
        obj.user = request.user.username
        super(StripAdmin, self).save_model(request, obj, form, change)


# admin.site.register(Oriented, OrientedAdmin)

class GameIconSwitchForm(forms.ModelForm):
    class Meta:
        widgets = {
            'imgLink': EnclosedInput(
                append='<button class="layui-btn layui-btn-xs"type="button" onclick="fun_imgLink(this)">预览</button><script language="javascript">\
                        function fun_imgLink (obj){\
                            var x = obj.previousSibling;; window.open(x.value);}</script>',
            ),
            'bi_landing_page': EnclosedInput(
                append='<button class="layui-btn layui-btn-xs"type="button" onclick="fun_bi_landing_page(this)">预览</button><script language="javascript">\
                    function fun_bi_landing_page (obj){\
                        var x = obj.previousSibling;; window.open(x.value);}</script>',
            ),
        }

class GameIconSwitchModelInline(admin.StackedInline):
    model = GameIconSwitchModel
    extra = 0
    max_num = 10
    form = GameIconSwitchForm
    fieldsets = [
        (
            '▼',
            {
                'fields': [
                    ('wxAppId', 'topath', 'scale'),
                    'imgLink',
                    ('weight', 'clickHide', 'openType'),
                    'bi_iconId',
                    'bi_landing_page_id',
                    'bi_educe_game',
                    'bi_landing_page',
                ],
                'classes': [
                    'collapse'
                ]
            }
        )]


class PositionModelInline(admin.StackedInline):
    model = PositionModel
    extra = 0
    fieldsets = [
        (
            '▼',
            {
                'fields': [
                    'position_id',
                    'type',
                    ('x', 'y'),
                ],
                'classes': [
                    'collapse'
                ]
            }
        )]

class IconSwitchForm(forms.ModelForm):
    class Meta:
        widgets = {
        }

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
    form = IconSwitchForm
    fieldsets = [
        (
            None,
            {
                'fields': [
                    'name',
                    'game_id',
                    'socket_url',
                    ('switch', 'framesInterval'),
                ]
            }
        )]

    list_per_page = 50

    save_as = True
    search_fields = ('name',)
    ordering = ('-id',)

    def game_name(self, obj):
        return allGame.get(obj.name, '')

    game_name.short_description = '游戏名称'

    def educe_game(self, obj):
        return get_iconswitch_name(obj.id)

    educe_game.short_description = '导出游戏'

    def save_model(self, request, obj, form, change):
        obj.user = request.user.username
        super(IconSwitchModelAdmin, self).save_model(request, obj, form, change)


class GameSlideOverForm(forms.ModelForm):
    class Meta:
        widgets = {
            'imgLink': EnclosedInput(
                append='<button class="layui-btn layui-btn-xs"type="button" onclick="fun_imgLink(this)">预览</button><script language="javascript">\
                        function fun_imgLink (obj){\
                            var x = obj.previousSibling;; window.open(x.value);}</script>',
            ),
            'bi_landing_page': EnclosedInput(
                append='<button class="layui-btn layui-btn-xs"type="button" onclick="fun_bi_landing_page(this)">预览</button><script language="javascript">\
                    function fun_bi_landing_page (obj){\
                        var x = obj.previousSibling;; window.open(x.value);}</script>',
            ),
        }

class GameSlideOverModelInline(admin.StackedInline):
    model = GameSlideOverModel
    extra = 0
    max_num = 10
    form = GameSlideOverForm
    fieldsets = [
        (
            '▼',
            {
                'fields': [
                    'index',
                    ('text', 'openUrl', 'topath'),
                    ('type', 'openType', 'isredon'),
                    'imgLink',
                    'bi_iconId',
                    'bi_landing_page_id',
                    'bi_educe_game',
                    'bi_landing_page',
                ],
                'classes': [
                    'collapse'
                ]
            }
        )]







class BgSlideOverForm(forms.ModelForm):
    class Meta:
        widgets = {
            'bt_imgurl': EnclosedInput(
                append='<button class="layui-btn layui-btn-xs"type="button" onclick="fun_bt_imgurl(this)">预览</button><script language="javascript">\
                        function fun_bt_imgurl (obj){\
                            var x = obj.previousSibling;; window.open(x.value);}</script>',
            ),
            'kuang_imgurl': EnclosedInput(
                append='<button class="layui-btn layui-btn-xs"type="button" onclick="fun_kuang_imgurl(this)">预览</button><script language="javascript">\
                                function fun_kuang_imgurl (obj){\
                                    var x = obj.previousSibling;; window.open(x.value);}</script>',
            ),
            'la_imgurl0': EnclosedInput(
                append='<button class="layui-btn layui-btn-xs"type="button" onclick="fun_la_imgurl0(this)">预览</button><script language="javascript">\
                                function fun_la_imgurl0 (obj){\
                                    var x = obj.previousSibling;; window.open(x.value);}</script>',
            ),
            'la_imgurl1': EnclosedInput(
                append='<button class="layui-btn layui-btn-xs"type="button" onclick="fun_la_imgurl1(this)">预览</button><script language="javascript">\
                                function fun_la_imgurl1 (obj){\
                                    var x = obj.previousSibling;; window.open(x.value);}</script>',
            ),
        }

class BgSlideOverModelInline(admin.StackedInline):
    model = BgSlideOverModel
    extra = 1
    min_num = 1
    max_num = 1
    form = BgSlideOverForm
    fieldsets = [
        (
            '标题',
            {
                'fields': [
                    ('bt_height', 'bt_scale', 'bt_yfromtop'),
                    'bt_imgurl',
                ],
                'classes': [
                    'collapse'
                ]
            }
        ),
        (
            '底框',
            {
                'fields': [
                    'kuang_positionY',
                    'kuang_bottomBlkHeight',
                    'kuang_imgurl'
                ],
                'classes': [
                    'collapse'
                ]
            }
        ),
        (
            '按钮',
            {
                'fields': [
                    ('la_positionX', 'la_positionY'),
                    ('la_scale', 'la_isredon'),
                    'la_imgurl0',
                    'la_imgurl1',
                ],
                'classes': [
                    'collapse'
                ]
            }
        ),
        (
            'icon布局',
            {
                'fields': [
                    ('icon_iconsWidth', 'icon_iconsHeight'),
                    ('icon_spacingX', 'icon_spacingY'),
                    ('icon_paddingLeft', 'icon_paddingRight')
                ],
                'classes': [
                    'collapse'
                ]
            }
        ),
        (
            '文本',
            {
                'fields': [
                    ('text_size', 'text_yfromIcon'),
                    ('text_colorR', 'text_colorG', 'text_colorB')
                ],
                'classes': [
                    'collapse'
                ]
            }
        )
    ]



class SlideOverForm(forms.ModelForm):
    class Meta:
        widgets = {
            'reddot': EnclosedInput(
                append='<button class="layui-btn layui-btn-xs"type="button" onclick="fun_reddot(this)">预览</button><script language="javascript">\
                        function fun_reddot (obj){\
                            var x = obj.previousSibling;; window.open(x.value);}</script>',
            ),
            'mask': EnclosedInput(
                append='<button class="layui-btn layui-btn-xs"type="button" onclick="fun_mask(this)">预览</button><script language="javascript">\
                                function fun_mask (obj){\
                                    var x = obj.previousSibling;; window.open(x.value);}</script>',
            ),
        }

@admin.register(SlideOverModel)
class SlideOverModelAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ['id', 'game_name', 'educe_game', 'user', 'create_time', 'modifi_time']
    list_display_links = ['game_name']
    # 内联
    inlines = [
        BgSlideOverModelInline,
        GameSlideOverModelInline,
    ]
    form = SlideOverForm
    fieldsets = [
        (
            None,
            {
                'fields': [
                    'name',
                    'game_id',
                    'socket_url',
                    ('switch', 'fromWhere', 'viewAdCounts',),
                    'reddot',
                    'mask',
                ]
            }
        )]
    list_per_page = 50

    save_as = True
    search_fields = ('name',)
    ordering = ('-id',)

    def game_name(self, obj):
        return allGame.get(obj.name, '')

    game_name.short_description = '游戏名称'

    def educe_game(self, obj):
        return get_slideover_educe_name(obj.id)

    educe_game.short_description = '导出游戏'

    def save_model(self, request, obj, form, change):
        obj.user = request.user.username
        super(SlideOverModelAdmin, self).save_model(request, obj, form, change)
