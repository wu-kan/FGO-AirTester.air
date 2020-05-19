# -*- encoding=utf8 -*-
__author__ = "wukan"

from airtest.core.api import *

auto_setup(__file__)

while(True):
    sleep(),touch(wait(Template(r"tpl1589881548920.png", record_pos=(0.109, -0.02), resolution=(1280, 720))))
    for i in range(1,4):
        for j in range(7):
            sleep(0.2),touch([j*130+140,i*130+250])
    sleep(),touch(wait(Template(r"tpl1583716275273.png", record_pos=(0.402, 0.241), resolution=(1280, 720))))
    sleep(),touch(wait(Template(r"tpl1589881387545.png", record_pos=(0.362, 0.248), resolution=(1280, 720))))
    sleep(),touch(wait(Template(r"tpl1583716275273.png", record_pos=(0.402, 0.241), resolution=(1280, 720))))
    for i in range(9):
        sleep(0.2),touch([3*130+140,3*130+250])
