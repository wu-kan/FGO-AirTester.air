# -*- encoding=utf8 -*-
__author__ = "wukan"

from airtest.core.api import *

auto_setup(__file__)

def wk_fuben():
    wait(Template(r"tpl1590311341656.png", record_pos=(0.191, -0.163), resolution=(1280, 720)),timeout=60)
    sleep(3),touch(wait(Template(r"tpl1590311341656.png", record_pos=(0.191, -0.163), resolution=(1280, 720)),timeout=60))
    return


def wk_zhuzhan():
    while not exists(Template(r"tpl1589876025431.png", record_pos=(-0.068, 0.259), resolution=(1280, 720))):
        sleep(10)
        if exists(Template(r"tpl1589876025431.png", record_pos=(-0.068, 0.259), resolution=(1280, 720))):
            break
        touch(wait(Template(r"tpl1579023156387.png", record_pos=(0.166, -0.18), resolution=(1280, 720))))
        sleep(3)
        touch(wait(Template(r"tpl1579023184729.png", record_pos=(0.155, 0.158), resolution=(1280, 720))))
    sleep(3)
    touch(wait(Template(r"tpl1589876025431.png", record_pos=(-0.068, 0.259), resolution=(1280, 720))))
    sleep(3)
    touch(wait(Template(r"tpl1578911889234.png", record_pos=(0.254, 0.184), resolution=(2520, 1080))))
    return

def wk_huanren():
    
    sleep(3),touch(wait(Template(r"tpl1579024428359.png", record_pos=(0.43, -0.031), resolution=(1280, 720))))

    
    sleep(3),touch(wait(Template(r"tpl1579336656280.png", record_pos=(0.345, -0.042), resolution=(1280, 720))))
    sleep(3),touch(wait(Template(r"tpl1589889389828.png", record_pos=(-0.391, 0.006), resolution=(1280, 720))))
    sleep(3),touch(wait(Template(r"tpl1589877073689.png", record_pos=(0.388, 0.002), resolution=(1280, 720))))
    sleep(3),touch(wait(Template(r"tpl1578907025095.png", record_pos=(-0.051, 0.156), resolution=(2520, 1080))))
    return

def wk_pingguo():
    sleep(3)
    if exists(Template(r"tpl1589874657349.png", record_pos=(-0.208, 0.089), resolution=(1280, 720))):
        touch(wait(Template(r"tpl1589874657349.png", record_pos=(-0.208, 0.089), resolution=(1280, 720))))
        touch(wait(Template(r"tpl1578909613574.png", record_pos=(0.066, 0.116), resolution=(2520, 1080))))
        return True
    
    sleep(3)
    if exists(Template(r"tpl1589874715811.png", record_pos=(-0.207, -0.031), resolution=(1280, 720))):
        touch(wait(Template(r"tpl1589874715811.png", record_pos=(-0.207, -0.031), resolution=(1280, 720))))
        touch(wait(Template(r"tpl1578909613574.png", record_pos=(0.066, 0.116), resolution=(2520, 1080))))
        return True
    return False

def wk_finish():
    while not exists(Template(r"tpl1578909199900.png", record_pos=(-0.051, 0.171), resolution=(2520, 1080))):
        sleep(60)
        if exists(Template(r"tpl1578909199900.png", record_pos=(-0.051, 0.171), resolution=(2520, 1080))):
            break
        for _iter in range(3):
            if exists(Template(r"tpl1578907166241.png", record_pos=(0.237, 0.139), resolution=(2520, 1080))):
                sleep(3)
        sleep(3),touch(wait(Template(r"tpl1578907166241.png", record_pos=(0.237, 0.139), resolution=(2520, 1080))))
        for _i in range(3):
            sleep(3),touch(wait(Template(r"tpl1589878497737.png", record_pos=(-0.167, 0.166), resolution=(1280, 720))))
    while not exists(Template(r"tpl1578908151840.png", record_pos=(0.226, 0.185), resolution=(2520, 1080))):
        sleep(3)
        if exists(Template(r"tpl1578909199900.png", record_pos=(-0.051, 0.171), resolution=(2520, 1080))):
            touch(wait(Template(r"tpl1578909199900.png", record_pos=(-0.051, 0.171), resolution=(2520, 1080))))
    touch(wait(Template(r"tpl1578908151840.png", record_pos=(0.226, 0.185), resolution=(2520, 1080))))
    for _i in range(3):
        sleep(3)
        if exists(Template(r"tpl1578908209107.png", record_pos=(-0.235, 0.149), resolution=(2520, 1080))):
            touch(wait(Template(r"tpl1578908209107.png", record_pos=(-0.235, 0.149), resolution=(2520, 1080))))
            break
    return

while True:
    wk_fuben()
    wk_pingguo()
    wk_zhuzhan()
    sleep(3),touch(wait(Template(r"tpl1589876861313.png", record_pos=(-0.445, 0.17), resolution=(1280, 720)),timeout=60))
    sleep(3),touch(wait(Template(r"tpl1589889071443.png", record_pos=(-0.373, 0.17), resolution=(1280, 720))))
    
    wk_huanren()
    sleep(3),touch(wait(Template(r"tpl1579024428359.png", record_pos=(0.43, -0.031), resolution=(1280, 720))))
    sleep(3),touch(wait(Template(r"tpl1589878189444.png", record_pos=(0.209, -0.04), resolution=(1280, 720))))
    
    while not exists(Template(r"tpl1589877321730.png", record_pos=(0.002, -0.125), resolution=(1280, 720))):
        sleep(3),touch(wait(Template(r"tpl1589877257986.png", record_pos=(-0.298, 0.169), resolution=(1280, 720)),timeout=60))
    sleep(3),touch(wait(Template(r"tpl1589877400699.png", record_pos=(0.22, 0.071), resolution=(1280, 720))))
    sleep(3),touch(wait(Template(r"tpl1589876861313.png", record_pos=(-0.445, 0.17), resolution=(1280, 720))))
    
    
    sleep(3),touch(wait(Template(r"tpl1589877652755.png", record_pos=(-0.052, 0.17), resolution=(1280, 720))))
    sleep(3),touch(wait(Template(r"tpl1589877800257.png", record_pos=(-0.124, 0.169), resolution=(1280, 720))))
    
    for _iter in range(2):
        sleep(3),touch(wait(Template(r"tpl1589877543257.png", record_pos=(-0.197, 0.17), resolution=(1280, 720))))
    

    sleep(3),touch(wait(Template(r"tpl1578907166241.png", record_pos=(0.237, 0.139), resolution=(2520, 1080))))
    sleep(3),touch(wait(Template(r"tpl1589878351581.png", record_pos=(0.191, -0.057), resolution=(1280, 720))))

    sleep(3),touch(wait(Template(r"tpl1589878292371.png", record_pos=(0.001, -0.078), resolution=(1280, 720))))
    sleep(3),touch(wait(Template(r"tpl1589878497737.png", record_pos=(-0.167, 0.166), resolution=(1280, 720))))
    wk_finish()