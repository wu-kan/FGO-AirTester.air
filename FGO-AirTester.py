# -*- encoding=utf8 -*-
__author__ = "wukan"

from airtest.core.api import *

auto_setup(__file__)

while(True):
    sleep(3)
    while not exists(Template(r"tpl1589882085891.png", record_pos=(0.148, -0.07), resolution=(1280, 720))):
        touch([3*130+140,3*130+250])
    sleep(3),touch(Template(r"tpl1589882085891.png", record_pos=(0.148, -0.07), resolution=(1280, 720)))
    for i in range(1,4):
        for j in range(7):
            sleep(0.2),touch([j*130+140,i*130+250])
    sleep(3),touch(wait(Template(r"tpl1583716275273.png", record_pos=(0.402, 0.241), resolution=(1280, 720))))
    sleep(3),touch(wait(Template(r"tpl1589881387545.png", record_pos=(0.362, 0.248), resolution=(1280, 720))))
    sleep(3),touch(wait(Template(r"tpl1589886761355.png", record_pos=(0.158, 0.18), resolution=(1280, 720))))
