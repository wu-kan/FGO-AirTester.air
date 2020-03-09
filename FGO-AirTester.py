# -*- encoding=utf8 -*-
__author__ = "wukan"

from airtest.core.api import *

auto_setup(__file__)

while(True):
    for i in range(4):
        for j in range(7):
            sleep(0.2)
            touch([j*130+140,i*130+250])
    sleep()
    touch(wait(Template(r"tpl1583716275273.png", record_pos=(0.402, 0.241), resolution=(1280, 720))))
    sleep()
    touch(wait(Template(r"tpl1583716252169.png", record_pos=(0.155, 0.176), resolution=(1280, 720))))
    sleep()
    touch(wait(Template(r"tpl1583716162753.png", record_pos=(0.002, 0.177), resolution=(1280, 720))))
