# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from common.config import (
    WXAPPID_CHOICES,
    SOCKET_URL,
    OWN_WXAPPID_CHOICE,
    OWN_WXAPPID_CONFIG,
    WXAPPID_CONFIG,
)

class StripModel(models.Model):
    game_id = models.PositiveIntegerField(verbose_name='gameId')
    name = models.CharField(verbose_name='游戏名称', choices=OWN_WXAPPID_CHOICE, max_length=255)
    socket_url = models.PositiveIntegerField(verbose_name='服务器', choices=SOCKET_URL)
    label = models.CharField(verbose_name='标题', max_length=512)
    bg = models.CharField(verbose_name='背景图', max_length=512)
    reddot = models.CharField(verbose_name='角标', max_length=512)
    spacingX = models.PositiveIntegerField(verbose_name='间距')
    iconWidth = models.PositiveIntegerField(verbose_name='宽度')
    iconHeight = models.PositiveIntegerField(verbose_name='高度')
    switch = models.PositiveIntegerField(verbose_name='switch', default=1)
    viewAdCounts = models.PositiveIntegerField(verbose_name='viewAdCounts', default=5)
    framesInterval = models.PositiveIntegerField(verbose_name='播放速度', default=50)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    modifi_time = models.DateTimeField('最后修改时间', auto_now=True)
    user = models.CharField(editable=False, null=True, verbose_name='操作人', max_length=255)

    online_modifi_time = models.DateTimeField('线上最后修改时间', editable=False, null=True)
    online_user = models.CharField(editable=False, null=True, verbose_name='推送操作人', max_length=255)

    def __str__(self):
        return OWN_WXAPPID_CONFIG.get(self.name, '')

    class Meta:
        verbose_name = '导流条'
        verbose_name_plural = verbose_name


class GameStripModel(models.Model):
    index = models.PositiveIntegerField(verbose_name='序号', help_text='输入数字')
    wxAppId = models.CharField(verbose_name="wxAppId", choices=WXAPPID_CHOICES, max_length=20)

    imgLink = models.CharField(verbose_name="ICON", max_length=512)
    topath = models.CharField(verbose_name='topath', max_length=512)
    isClickHide = models.BooleanField(verbose_name='是否隐藏')
    foreignkey_strip = models.ForeignKey(StripModel, verbose_name="导流条")

    bi_iconId = models.CharField(verbose_name='bI_IconId',  max_length=10)
    bi_landing_page = models.CharField(verbose_name='bI_落地页', max_length=512)
    bi_landing_page_id = models.CharField(verbose_name='bI_落地页Id', max_length=10)
    bi_educe_game = models.CharField(verbose_name='bI_渠道标识', max_length=10)

    def __str__(self):
        return WXAPPID_CONFIG.get(self.wxAppId, '')

    class Meta:
        verbose_name = '导出游戏'
        verbose_name_plural = verbose_name


class IconSwitchModel(models.Model):
    game_id = models.PositiveIntegerField(verbose_name='gameId')
    name = models.CharField(verbose_name='游戏名称', choices=OWN_WXAPPID_CHOICE, max_length=255)
    socket_url = models.PositiveIntegerField(verbose_name='服务器', choices=SOCKET_URL)
    switch = models.PositiveIntegerField(verbose_name='switch', default=1)
    framesInterval = models.PositiveIntegerField(verbose_name='播放速度', default=10000)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    modifi_time = models.DateTimeField('最后修改时间', auto_now=True)
    user = models.CharField(editable=False, null=True, verbose_name='操作人', max_length=255)

    online_modifi_time = models.DateTimeField('线上最后修改时间', editable=False, null=True)
    online_user = models.CharField(editable=False, null=True, verbose_name='推送操作人', max_length=255)

    def __str__(self):
        return OWN_WXAPPID_CONFIG.get(self.name, '')

    class Meta:
        verbose_name = 'Icon切换'
        verbose_name_plural = verbose_name

class PositionModel(models.Model):
    position_id = models.IntegerField(verbose_name='id')
    type = models.IntegerField(verbose_name='type')
    x = models.FloatField(verbose_name='x')
    y = models.FloatField(verbose_name='y')
    foreignkey_iconswitch = models.ForeignKey(IconSwitchModel, verbose_name="Icon切换")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '位置设定'
        verbose_name_plural = verbose_name


class GameIconSwitchModel(models.Model):
    wxAppId = models.CharField(verbose_name="wxAppId", choices=WXAPPID_CHOICES, max_length=20)
    weight = models.PositiveIntegerField(verbose_name='权重')
    scale = models.FloatField(verbose_name='缩放比例')
    imgLink = models.CharField(verbose_name="ICON", max_length=512)
    openType = models.BooleanField(verbose_name='打开方式', default=1)
    clickHide = models.BooleanField(verbose_name='是否隐藏')
    topath = models.CharField(verbose_name='topath', max_length=512)
    foreignkey_iconswitch = models.ForeignKey(IconSwitchModel, verbose_name="Icon切换")

    bi_iconId = models.CharField(verbose_name='bI_IconId',  max_length=10)
    bi_landing_page = models.CharField(verbose_name='bI_落地页', max_length=512)
    bi_landing_page_id = models.CharField(verbose_name='bI_落地页Id', max_length=10)
    bi_educe_game = models.CharField(verbose_name='bI_渠道标识', max_length=10)

    def __str__(self):
        return WXAPPID_CONFIG.get(self.wxAppId, '')

    class Meta:
        verbose_name = '导出游戏'
        verbose_name_plural = verbose_name


class SlideOverModel(models.Model):
    game_id = models.PositiveIntegerField(verbose_name='gameId')
    name = models.CharField(verbose_name='游戏名称', choices=OWN_WXAPPID_CHOICE, max_length=255)
    socket_url = models.PositiveIntegerField(verbose_name='服务器', choices=SOCKET_URL)
    switch = models.PositiveIntegerField(verbose_name='switch', default=1)
    fromWhere = models.PositiveIntegerField(verbose_name='展开方向', default=0)

    reddot = models.CharField(verbose_name='角标', max_length=512, default='https://sanxqn.nalrer.cn/tysanxiao/test/LikeConfigRes/reddot.png')
    mask = models.CharField(verbose_name='蒙层', max_length=512, default='https://sanxqn.nalrer.cn/tysanxiao/test/LikeConfigRes/adRes.png')
    viewAdCounts = models.PositiveIntegerField(verbose_name='viewAdCounts', default=3)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    modifi_time = models.DateTimeField('最后修改时间', auto_now=True)
    user = models.CharField(editable=False, null=True, verbose_name='操作人', max_length=255)

    online_modifi_time = models.DateTimeField('线上最后修改时间', editable=False, null=True)
    online_user = models.CharField(editable=False, null=True, verbose_name='推送操作人', max_length=255)

    def __str__(self):
        return OWN_WXAPPID_CONFIG.get(self.name, '')

    class Meta:
        verbose_name = '侧拉框'
        verbose_name_plural = verbose_name

class BgSlideOverModel(models.Model):
    # 标题 4
    bt_height = models.PositiveIntegerField(verbose_name='高度')
    bt_scale = models.FloatField(verbose_name='缩放比例')
    bt_yfromtop = models.PositiveIntegerField(verbose_name='图片中心点离上方距离')
    bt_imgurl = models.CharField(verbose_name='标题ICON', max_length=512)

    # 框 3
    kuang_positionY = models.FloatField(verbose_name='框中心点占整个屏幕比例')
    kuang_bottomBlkHeight = models.PositiveIntegerField(verbose_name='框内的下方空白高')
    kuang_imgurl = models.CharField(verbose_name='框背景图', max_length=512)

    # 拉按钮 6
    la_scale = models.FloatField(verbose_name='缩放比例')
    la_positionX = models.FloatField(verbose_name='positionX')
    la_positionY = models.FloatField(verbose_name='positionY')
    la_imgurl0 = models.CharField(verbose_name='未拉取时图', max_length=512)
    la_imgurl1 = models.CharField(verbose_name='拉取时图', max_length=512)
    la_isredon = models.BooleanField(verbose_name='显示红点', default=1)

    # icon布局 6
    icon_iconsWidth = models.IntegerField(verbose_name='iconsWidth')
    icon_iconsHeight = models.IntegerField(verbose_name='iconsHeight')
    icon_spacingX = models.IntegerField(verbose_name='spacingX')
    icon_spacingY = models.IntegerField(verbose_name='spacingY')
    icon_paddingLeft = models.IntegerField(verbose_name='paddingLeft')
    icon_paddingRight = models.IntegerField(verbose_name='paddingRight')

    # 文本 5
    text_size = models.PositiveIntegerField(verbose_name='size')
    text_yfromIcon = models.PositiveIntegerField(verbose_name='yfromIcon')
    text_colorR = models.PositiveIntegerField(verbose_name='colorR')
    text_colorG = models.PositiveIntegerField(verbose_name='colorG')
    text_colorB = models.PositiveIntegerField(verbose_name='colorB')

    foreignkey_labelSlideOver = models.OneToOneField(SlideOverModel, verbose_name="侧拉框")

    def __str__(self):
        return '背景框'

    class Meta:
        verbose_name = '背景框'
        verbose_name_plural = verbose_name




class GameSlideOverModel(models.Model):
    index = models.PositiveIntegerField(verbose_name='序号', help_text='输入数字')
    text = models.CharField(verbose_name='text',max_length=512)
    type = models.BooleanField(verbose_name='动图icon', default=0)
    imgLink = models.CharField(verbose_name="ICON", max_length=512)
    openType = models.BooleanField(verbose_name='打开方式', default=1)
    openUrl = models.CharField(verbose_name="wxAppId", choices=WXAPPID_CHOICES, max_length=20)
    isredon = models.BooleanField(verbose_name='显示红点', default=1)
    topath = models.CharField(verbose_name='topath', max_length=512)
    foreignkey_labelSlideOver = models.ForeignKey(SlideOverModel, verbose_name="侧拉框")

    bi_iconId = models.CharField(verbose_name='bI_IconId',  max_length=10)
    bi_landing_page = models.CharField(verbose_name='bI_落地页', max_length=512)
    bi_landing_page_id = models.CharField(verbose_name='bI_落地页Id', max_length=10)
    bi_educe_game = models.CharField(verbose_name='bI_渠道标识', max_length=10)

    def __str__(self):
        return WXAPPID_CONFIG.get(self.openUrl, '')

    class Meta:
        verbose_name = '导出游戏'
        verbose_name_plural = verbose_name


