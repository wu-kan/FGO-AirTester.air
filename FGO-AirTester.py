# -*- encoding=utf8 -*-
__author__ = "wukan"
from airtest.core.api import *
auto_setup(__file__)


def wk_pingguo():
    sleep(3)
    if exists(Template(r"tpl1589874657349.png", record_pos=(-0.208, 0.089), resolution=(1280, 720))):
        sleep(3), touch(wait(Template(r"tpl1589874657349.png",
                                      record_pos=(-0.208, 0.089), resolution=(1280, 720))))
        sleep(3), touch(wait(Template(r"tpl1578909613574.png",
                                      record_pos=(0.066, 0.116), resolution=(2520, 1080))))
        return True
    sleep(3)
    if exists(Template(r"tpl1589874715811.png", record_pos=(-0.207, -0.031), resolution=(1280, 720))):
        sleep(3), touch(wait(Template(r"tpl1589874715811.png",
                                      record_pos=(-0.207, -0.031), resolution=(1280, 720))))
        sleep(3), touch(wait(Template(r"tpl1578909613574.png",
                                      record_pos=(0.066, 0.116), resolution=(2520, 1080))))
        return True
    return False


while True:
    wait(Template(r"tpl1578907166241.png",
                  record_pos=(0.237, 0.139), resolution=(2520, 1080)), timeout=40)
    sleep(3), touch(wait(Template(r"tpl1639813231898.png", record_pos=(
        0.431, -0.041), resolution=(1280, 720))))
    sleep(6), touch(v=[1080, 300])
    sleep(3), touch(wait(Template(r"tpl1639813423412.png",
                                  record_pos=(0.236, 0.108), resolution=(1280, 720))))
    sleep(6), touch(v=[700, 580])
    for i in range(2):
        sleep(6), touch(v=[250+300*i, 580])
        sleep(3), touch(wait(Template(r"tpl1639813423412.png",
                                      record_pos=(0.236, 0.108), resolution=(1280, 720))))
        sleep(3), touch(wait(Template(r"tpl1639815779677.png",
                                      record_pos=(-0.373, 0.186), resolution=(1280, 720))))
        sleep(3), touch(wait(Template(r"tpl1639813423412.png",
                                      record_pos=(0.236, 0.108), resolution=(1280, 720))))
    sleep(3), touch(wait(Template(r"tpl1578907166241.png",
                                  record_pos=(0.237, 0.139), resolution=(2520, 1080))))
    sleep(3), touch(wait(Template(r"tpl1639814841571.png",
                                  record_pos=(0.184, -0.082), resolution=(1280, 720))))
    for _i in range(2):
        sleep(3), touch(wait(Template(r"tpl1639815082391.png",
                                      record_pos=(0.025, 0.169), resolution=(1280, 720))))
    sleep(3), touch(wait(Template(r"tpl1639815289915.png",
                                  record_pos=(-0.442, 0.184), resolution=(1280, 720)), timeout=40))
    sleep(3), touch(wait(Template(r"tpl1578907166241.png",
                                  record_pos=(0.237, 0.139), resolution=(2520, 1080))))
    sleep(3), touch(wait(Template(r"tpl1639814841571.png",
                                  record_pos=(0.184, -0.082), resolution=(1280, 720))))
    for _i in range(2):
        sleep(3), touch(wait(Template(r"tpl1639815082391.png",
                                      record_pos=(0.025, 0.169), resolution=(1280, 720))))
    sleep(3), touch(wait(Template(r"tpl1639815289915.png",
                                  record_pos=(-0.442, 0.184), resolution=(1280, 720)), timeout=40))
    sleep(3), touch(wait(Template(r"tpl1639815431400.png",
                                  record_pos=(0.191, 0.186), resolution=(1280, 720))))
    sleep(3), touch(wait(Template(r"tpl1578907166241.png",
                                  record_pos=(0.237, 0.139), resolution=(2520, 1080))))
    sleep(3), touch(wait(Template(r"tpl1639814841571.png",
                                  record_pos=(0.184, -0.082), resolution=(1280, 720))))
    for _i in range(2):
        sleep(3), touch(wait(Template(r"tpl1639815082391.png",
                                      record_pos=(0.025, 0.169), resolution=(1280, 720))))
    while not exists(Template(r"tpl1578909199900.png", record_pos=(-0.051, 0.171), resolution=(2520, 1080))):
        sleep(40)
        if exists(Template(r"tpl1578909199900.png", record_pos=(-0.051, 0.171), resolution=(2520, 1080))):
            break
        for _iter in range(3):
            if exists(Template(r"tpl1578907166241.png", record_pos=(0.237, 0.139), resolution=(2520, 1080))):
                sleep(3)
        sleep(3), touch(wait(Template(r"tpl1578907166241.png",
                                      record_pos=(0.237, 0.139), resolution=(2520, 1080))))
        for _i in range(3):
            sleep(3), touch(wait(Template(r"tpl1639815082391.png", record_pos=(
                0.025, 0.169), resolution=(1280, 720)), timeout=40))
    while not exists(Template(r"tpl1578908151840.png", record_pos=(0.226, 0.185), resolution=(2520, 1080))):
        sleep(3)
        if exists(Template(r"tpl1578909199900.png", record_pos=(-0.051, 0.171), resolution=(2520, 1080))):
            touch(wait(Template(r"tpl1578909199900.png",
                                record_pos=(-0.051, 0.171), resolution=(2520, 1080))))
        if exists(Template(r"tpl1602601373299.png", record_pos=(-0.468, -0.249), resolution=(1280, 720))):
            touch(wait(Template(r"tpl1602601373299.png",
                                record_pos=(-0.468, -0.249), resolution=(1280, 720))))
    sleep(3), touch(wait(Template(r"tpl1578908151840.png",
                                  record_pos=(0.226, 0.185), resolution=(2520, 1080))))
    sleep(3)
    if exists(Template(r"tpl1602327527046.png", record_pos=(-0.236, 0.199), resolution=(1280, 720))):
        sleep(3), touch(wait(Template(r"tpl1602327527046.png",
                                      record_pos=(-0.236, 0.199), resolution=(1280, 720))))
    sleep(3), touch(wait(Template(r"tpl1600700045702.png",
                                  record_pos=(0.154, 0.163), resolution=(1280, 720))))
    wk_pingguo()
    while not exists(Template(r"tpl1639812757205.png", record_pos=(-0.137, -0.046), resolution=(1280, 720))):
        sleep(10)
        if exists(Template(r"tpl1639812757205.png", record_pos=(-0.137, -0.046), resolution=(1280, 720))):
            break
        sleep(3), touch(wait(Template(r"tpl1579023156387.png",
                                      record_pos=(0.166, -0.18), resolution=(1280, 720))))
        sleep(3), touch(wait(Template(r"tpl1579023184729.png",
                                      record_pos=(0.155, 0.158), resolution=(1280, 720))))
    sleep(3), touch(wait(Template(r"tpl1639812757205.png",
                                  record_pos=(-0.137, -0.046), resolution=(1280, 720))))
