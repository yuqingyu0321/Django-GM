# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from common.config import WXAPPID_CHOICES, SOCKET_URL





class StripModel(models.Model):
    game_id = models.PositiveIntegerField(verbose_name='gameId', unique=True)
    name = models.CharField(verbose_name='游戏名称', max_length=255, unique=True)
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

    def __str__(self):
        return self.name

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
    bi_educe_game = models.CharField(verbose_name='bI_内部path', max_length=10)

    def __str__(self):
        name = ''
        for i in WXAPPID_CHOICES:
            if i[0] == self.wxAppId:
                name = i[1]
                break
        return name

    class Meta:
        verbose_name = '导出游戏'
        verbose_name_plural = verbose_name


class IconSwitchModel(models.Model):
    game_id = models.PositiveIntegerField(verbose_name='gameId', unique=True)
    name = models.CharField(verbose_name='游戏名称', max_length=255, unique=True)
    socket_url = models.PositiveIntegerField(verbose_name='服务器', choices=SOCKET_URL)
    switch = models.PositiveIntegerField(verbose_name='switch', default=1)
    framesInterval = models.PositiveIntegerField(verbose_name='播放速度', default=10000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Icon切换'
        verbose_name_plural = verbose_name

class PositionModel(models.Model):
    position_id = models.IntegerField(verbose_name='id')
    type = models.IntegerField(verbose_name='type')
    x = models.IntegerField(verbose_name='x')
    y = models.IntegerField(verbose_name='y')
    foreignkey_iconswitch = models.ForeignKey(IconSwitchModel, verbose_name="Icon切换")

    def __str__(self):
        return ''

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
    bi_educe_game = models.CharField(verbose_name='bI_内部path', max_length=10)

    def __str__(self):
        name = ''
        for i in WXAPPID_CHOICES:
            if i[0] == self.wxAppId:
                name = i[1]
                break
        return name

    class Meta:
        verbose_name = '导出游戏'
        verbose_name_plural = verbose_name


class SlideOverModel(models.Model):
    game_id = models.PositiveIntegerField(verbose_name='gameId', unique=True)
    name = models.CharField(verbose_name='游戏名称', max_length=255, unique=True)
    socket_url = models.PositiveIntegerField(verbose_name='服务器', choices=SOCKET_URL)
    switch = models.PositiveIntegerField(verbose_name='switch', default=1)
    fromWhere = models.PositiveIntegerField(verbose_name='展开方向', default=0)

    reddot = models.CharField(verbose_name='角标', max_length=512, default='https://sanxqn.nalrer.cn/tysanxiao/test/LikeConfigRes/reddot.png')
    mask = models.CharField(verbose_name='蒙层', max_length=512, default='https://sanxqn.nalrer.cn/tysanxiao/test/LikeConfigRes/adRes.png')
    viewAdCounts = models.PositiveIntegerField(verbose_name='viewAdCounts', default=3)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '侧拉框'
        verbose_name_plural = verbose_name

class LabelSlideOverModel(models.Model):
    height = models.PositiveIntegerField(verbose_name='高度')
    scale = models.FloatField(verbose_name='缩放比例')
    yfromtop = models.PositiveIntegerField(verbose_name='图片中心点离上方距离')
    imgurl = models.CharField(verbose_name='标题ICON', max_length=512)
    foreignkey_labelSlideOver = models.OneToOneField(SlideOverModel, verbose_name="侧拉框")

    def __str__(self):
        return '标题'

    class Meta:
        verbose_name = '标题'
        verbose_name_plural = verbose_name


class PullSlideOverModel(models.Model):
    scale = models.FloatField(verbose_name='缩放比例')
    positionX = models.FloatField(verbose_name='positionX')
    positionY = models.FloatField(verbose_name='positionY')
    imgurl0 = models.CharField(verbose_name='未拉取时图', max_length=512)
    imgurl1 = models.CharField(verbose_name='拉取时图', max_length=512)
    isredon = models.BooleanField(verbose_name='显示红点', default=1)
    foreignkey_labelSlideOver = models.OneToOneField(SlideOverModel, verbose_name="侧拉框")

    def __str__(self):
        return '拉按钮'

    class Meta:
        verbose_name = '拉按钮'
        verbose_name_plural = verbose_name

class BgSlideOverModel(models.Model):
    positionY = models.FloatField(verbose_name='positionY_框中心点占整个屏幕的比例')
    bottomBlkHeight = models.PositiveIntegerField(verbose_name='框内的下方空白的高')
    imgurl = models.CharField(verbose_name='框的背景图', max_length=512)
    foreignkey_labelSlideOver = models.OneToOneField(SlideOverModel, verbose_name="侧拉框")

    def __str__(self):
        return '框'

    class Meta:
        verbose_name = '框'
        verbose_name_plural = verbose_name


class GridSlideOverModel(models.Model):
    iconsWidth = models.IntegerField(verbose_name='iconsWidth')
    iconsHeight = models.IntegerField(verbose_name='iconsHeight')
    spacingX = models.IntegerField(verbose_name='spacingX')
    spacingY = models.IntegerField(verbose_name='spacingY')
    paddingLeft = models.IntegerField(verbose_name='paddingLeft')
    paddingRight = models.IntegerField(verbose_name='paddingRight')
    foreignkey_labelSlideOver = models.OneToOneField(SlideOverModel, verbose_name="侧拉框")

    def __str__(self):
        return 'Icon布局'

    class Meta:
        verbose_name = 'Icon布局'
        verbose_name_plural = verbose_name


class TextSlideOverModel(models.Model):
    size = models.PositiveIntegerField(verbose_name='size')
    yfromIcon = models.PositiveIntegerField(verbose_name='yfromIcon')
    colorR = models.PositiveIntegerField(verbose_name='colorR')
    colorG = models.PositiveIntegerField(verbose_name='colorG')
    colorB = models.PositiveIntegerField(verbose_name='colorB')
    foreignkey_labelSlideOver = models.OneToOneField(SlideOverModel, verbose_name="侧拉框")

    def __str__(self):
        return '文本'

    class Meta:
        verbose_name = '文本'
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
    bi_educe_game = models.CharField(verbose_name='bI_内部path', max_length=10)

    def __str__(self):
        name = ''
        for i in WXAPPID_CHOICES:
            if i[0] == self.openUrl:
                name = i[1]
                break
        return name

    class Meta:
        verbose_name = '导出游戏'
        verbose_name_plural = verbose_name


