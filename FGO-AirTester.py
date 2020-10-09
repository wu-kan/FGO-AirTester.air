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
    sleep(3), touch(wait(Template(r"tpl1600698514070.png",
                                  record_pos=(-0.295, 0.171), resolution=(1280, 720)), timeout=60))
    sleep(3), touch(wait(Template(r"tpl1578907166241.png",
                                  record_pos=(0.237, 0.139), resolution=(2520, 1080))))
    sleep(3), touch(wait(Template(r"tpl1600696319040.png",
                                  record_pos=(-0.173, -0.078), resolution=(1280, 720))))
    for _i in range(2):
        sleep(3), touch(wait(Template(r"tpl1589878497737.png",
                                      record_pos=(-0.167, 0.166), resolution=(1280, 720))))
    while not exists(Template(r"tpl1602234548578.png", record_pos=(0.114, -0.132), resolution=(1280, 720))):
        sleep(3)
        if exists(Template(r"tpl1602234548578.png", record_pos=(0.114, -0.132), resolution=(1280, 720))):
            break
        sleep(3), touch(wait(Template(r"tpl1600696910381.png",
                                      record_pos=(-0.199, 0.17), resolution=(1280, 720)), timeout=60))
    sleep(3), touch(wait(Template(r"tpl1600696705407.png", record_pos=(
        0.277, 0.034), resolution=(1280, 720)), timeout=60))
    sleep(3), touch(wait(Template(r"tpl1589876861313.png",
                                  record_pos=(-0.445, 0.17), resolution=(1280, 720))))
    sleep(3), touch(wait(Template(r"tpl1600697091352.png",
                                  record_pos=(-0.124, 0.171), resolution=(1280, 720))))
    sleep(3), touch(wait(Template(r"tpl1600698053723.png",
                                  record_pos=(0.196, 0.167), resolution=(1280, 720))))
    sleep(3), touch(wait(Template(r"tpl1579024428359.png",
                                  record_pos=(0.43, -0.031), resolution=(1280, 720))))

    sleep(3), touch(wait(Template(r"tpl1579336656280.png",
                                  record_pos=(0.345, -0.042), resolution=(1280, 720))))
    sleep(3), touch(wait(Template(r"tpl1600697202445.png",
                                  record_pos=(-0.234, -0.014), resolution=(1280, 720))))
    sleep(3), touch(wait(Template(r"tpl1600697813159.png",
                                  record_pos=(0.237, -0.012), resolution=(1280, 720))))
    sleep(3), touch(wait(Template(r"tpl1578907025095.png",
                                  record_pos=(-0.051, 0.156), resolution=(2520, 1080))))
    sleep(9)
    for _i in range(2):
        while not exists(Template(r"tpl1602234548578.png", record_pos=(0.114, -0.132), resolution=(1280, 720))):
            sleep(3)
            if exists(Template(r"tpl1602234548578.png", record_pos=(0.114, -0.132), resolution=(1280, 720))):
                break
            sleep(3), touch(wait(Template(r"tpl1600698375064.png",
                                          record_pos=(-0.197, 0.171), resolution=(1280, 720))))
        sleep(3), touch(wait(Template(r"tpl1600696705407.png", record_pos=(
            0.277, 0.034), resolution=(1280, 720)), timeout=60))

    while not exists(Template(r"tpl1602234548578.png", record_pos=(0.114, -0.132), resolution=(1280, 720))):
        sleep(3)
        if exists(Template(r"tpl1602234548578.png", record_pos=(0.114, -0.132), resolution=(1280, 720))):
            break
        sleep(3), touch(wait(Template(r"tpl1600698514070.png",
                                      record_pos=(-0.295, 0.171), resolution=(1280, 720))))
    sleep(3), touch(wait(Template(r"tpl1600696705407.png", record_pos=(
        0.277, 0.034), resolution=(1280, 720)), timeout=60))
    sleep(3), touch(wait(Template(r"tpl1578907166241.png",
                                  record_pos=(0.237, 0.139), resolution=(2520, 1080))))
    sleep(3), touch(wait(Template(r"tpl1600698596657.png",
                                  record_pos=(0.187, -0.07), resolution=(1280, 720))))
    for _i in range(2):
        sleep(3), touch(wait(Template(r"tpl1589878497737.png",
                                      record_pos=(-0.167, 0.166), resolution=(1280, 720))))
    sleep(3), touch(wait(Template(r"tpl1579024428359.png", record_pos=(
        0.43, -0.031), resolution=(1280, 720)), timeout=60))
    sleep(3), touch(wait(Template(r"tpl1589878189444.png",
                                  record_pos=(0.209, -0.04), resolution=(1280, 720))))
    for _i in range(2):
        sleep(3), touch(wait(Template(r"tpl1600698778724.png",
                                      record_pos=(-0.123, 0.168), resolution=(1280, 720))))
    sleep(3)
    while not exists(Template(r"tpl1602234548578.png", record_pos=(0.114, -0.132), resolution=(1280, 720))):
        sleep(3)
        if exists(Template(r"tpl1602234548578.png", record_pos=(0.114, -0.132), resolution=(1280, 720))):
            break
        sleep(6), touch(wait(Template(r"tpl1600698514070.png",
                                      record_pos=(-0.295, 0.171), resolution=(1280, 720))))
    sleep(3), touch(wait(Template(r"tpl1600696705407.png", record_pos=(
        0.277, 0.034), resolution=(1280, 720)), timeout=60))
    sleep(3), touch(wait(Template(r"tpl1578907166241.png",
                                  record_pos=(0.237, 0.139), resolution=(2520, 1080))))
    sleep(3), touch(wait(Template(r"tpl1600698596657.png",
                                  record_pos=(0.187, -0.07), resolution=(1280, 720))))
    for _i in range(2):
        sleep(3), touch(wait(Template(r"tpl1589878497737.png",
                                      record_pos=(-0.167, 0.166), resolution=(1280, 720))))
    while not exists(Template(r"tpl1578909199900.png", record_pos=(-0.051, 0.171), resolution=(2520, 1080))):
        sleep(60)
        if exists(Template(r"tpl1578909199900.png", record_pos=(-0.051, 0.171), resolution=(2520, 1080))):
            break
        for _iter in range(3):
            if exists(Template(r"tpl1578907166241.png", record_pos=(0.237, 0.139), resolution=(2520, 1080))):
                sleep(3)
        sleep(3), touch(wait(Template(r"tpl1578907166241.png",
                                      record_pos=(0.237, 0.139), resolution=(2520, 1080))))
        for _i in range(3):
            sleep(3), touch(wait(Template(r"tpl1589878497737.png",
                                          record_pos=(-0.167, 0.166), resolution=(1280, 720))))
    while not exists(Template(r"tpl1578908151840.png", record_pos=(0.226, 0.185), resolution=(2520, 1080))):
        sleep(3)
        if exists(Template(r"tpl1578909199900.png", record_pos=(-0.051, 0.171), resolution=(2520, 1080))):
            touch(wait(Template(r"tpl1578909199900.png",
                                record_pos=(-0.051, 0.171), resolution=(2520, 1080))))
    sleep(3), touch(wait(Template(r"tpl1578908151840.png",
                                  record_pos=(0.226, 0.185), resolution=(2520, 1080))))
    sleep(3), touch(wait(Template(r"tpl1600700045702.png",
                                  record_pos=(0.154, 0.163), resolution=(1280, 720))))
    wk_pingguo()
    while not exists(Template(r"tpl1600699219596.png", record_pos=(-0.07, -0.055), resolution=(1280, 720))):
        sleep(10)
        if exists(Template(r"tpl1600699219596.png", record_pos=(-0.07, -0.055), resolution=(1280, 720))):
            break
        sleep(3), touch(wait(Template(r"tpl1579023156387.png",
                                      record_pos=(0.166, -0.18), resolution=(1280, 720))))
        sleep(3), touch(wait(Template(r"tpl1579023184729.png",
                                      record_pos=(0.155, 0.158), resolution=(1280, 720))))
    sleep(3), touch(wait(Template(r"tpl1600699219596.png",
                                  record_pos=(-0.07, -0.055), resolution=(1280, 720))))
