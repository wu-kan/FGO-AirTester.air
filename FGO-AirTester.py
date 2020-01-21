# -*- encoding=utf8 -*-
__author__ = "wukan"

from airtest.core.api import *

auto_setup(__file__)

for _i in range(8):
    for _i in range(32):
        sleep(2.4)
        touch([450,450])
    touch(wait(Template(r"tpl1579452354002.png", record_pos=(0.387, -0.088), resolution=(1280, 720))))
    for _i in range(2):
        sleep(2.4)
        touch([750,580])