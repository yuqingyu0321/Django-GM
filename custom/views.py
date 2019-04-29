# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from gameInfo import game
from custom.view.iconConfigView import OrientedIconConfig, OrientedIconSub, OrientedIconPosition
from custom.view.stripConfigView import StripConfig, StripSub
from custom.view.slideoverConfigView import SlideoverConfig, SlideoverSub
from custom.view.pushView import PushView
from custom.view.endConfigView import EndConfig, EndConfigSub
__ALL__ = [
    OrientedIconConfig,
    OrientedIconSub,
    OrientedIconPosition,
    StripConfig,
    StripSub,
    SlideoverConfig,
    SlideoverSub,
    PushView,
    EndConfig,
    EndConfigSub,
]


def index(request):
    content = {
        'gameChoice': game.innerGame
    }
    return render(request, 'index.html', content)


def welcome(request):
    return render(request, 'welcome.html')
