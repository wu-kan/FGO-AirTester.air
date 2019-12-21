# -*- encoding=utf8 -*-
__author__ = "wukan"

from airtest.core.api import *
auto_setup(__file__)
for _iter in range(4):
    touch(wait(Template(r"tpl1576848245799.png", record_pos=(0.12, -0.069), resolution=(2520, 1080)),timeout=60))
    sleep()

    v=exists(Template(r"tpl1576851873721.png", record_pos=(-0.093, -0.02), resolution=(2520, 1080)))
    if v != False:
        touch(v)
        touch(wait(Template(r"tpl1576851988180.png", record_pos=(0.064, 0.12), resolution=(2520, 1080)))) # 恰苹果

    touch(wait(Template(r"tpl1576848308190.png", record_pos=(0.242, -0.027), resolution=(2520, 1080))))
    touch(wait(Template(r"tpl1576848397065.png", record_pos=(0.278, 0.19), resolution=(2520, 1080))))

    wait(Template(r"tpl1576850638587.png", record_pos=(0.242, 0.142), resolution=(2520, 1080)),timeout=60) # 等待攻击界面加载完成

    touch(v=(400,900)) # 艾蕾2技能
    touch(wait(Template(r"tpl1576850738968.png", record_pos=(0.075, 0.038), resolution=(2520, 1080))))


    touch(wait(Template(r"tpl1576850905314.png", record_pos=(-0.276, 0.127), resolution=(2520, 1080)))) # 艾蕾3技能
    touch(wait(Template(r"tpl1576850738968.png", record_pos=(0.075, 0.038), resolution=(2520, 1080))))

    touch(wait(Template(r"tpl1576852106640.png", record_pos=(-0.012, 0.127), resolution=(2520, 1080)))) # 弓凛1技能
    touch(wait(Template(r"tpl1576850738968.png", record_pos=(0.075, 0.038), resolution=(2520, 1080))))



    touch(wait(Template(r"tpl1576850638587.png", record_pos=(0.242, 0.142), resolution=(2520, 1080))))
    touch(wait(Template(r"tpl1576853632199.png", record_pos=(-0.18, -0.056), resolution=(2520, 1080))))
    sleep()
    touch(v=(350,900)) # 指令卡1
    sleep()
    touch(v=(750,900)) # 指令卡2
    sleep()
    snapshot(msg="艾蕾宝具动画")


    wait(Template(r"tpl1576850638587.png", record_pos=(0.242, 0.142), resolution=(2520, 1080)),timeout=60) # 等待攻击界面加载完成
    touch(v=(750,900)) # 小莫1技能
    touch(wait(Template(r"tpl1576850738968.png", record_pos=(0.075, 0.038), resolution=(2520, 1080))))
    touch(wait(Template(r"tpl1576851280803.png", record_pos=(-0.088, 0.127), resolution=(2520, 1080)))) # 小莫3技能
    touch(wait(Template(r"tpl1576850738968.png", record_pos=(0.075, 0.038), resolution=(2520, 1080))))

    touch(wait(Template(r"tpl1576851330274.png", record_pos=(0.099, 0.129), resolution=(2520, 1080)))) # 弓凛3技能
    touch(wait(Template(r"tpl1576850738968.png", record_pos=(0.075, 0.038), resolution=(2520, 1080))))
    touch(wait(Template(r"tpl1576850638587.png", record_pos=(0.242, 0.142), resolution=(2520, 1080))))

    touch(wait(Template(r"tpl1576853955975.png", record_pos=(-0.052, -0.052), resolution=(2520, 1080))))
    sleep()
    touch(v=(350,900)) # 指令卡1
    sleep()
    touch(v=(750,900)) # 指令卡2
    sleep()
    snapshot(msg="小莫宝具动画")

    touch(wait(Template(r"tpl1576851569748.png", record_pos=(0.043, 0.129), resolution=(2520, 1080)),timeout=60)) # 弓凛2技能
    touch(wait(Template(r"tpl1576850738968.png", record_pos=(0.075, 0.038), resolution=(2520, 1080))))
    touch(wait(Template(r"tpl1576850638587.png", record_pos=(0.242, 0.142), resolution=(2520, 1080))))
    touch(wait(Template(r"tpl1576854091829.png", record_pos=(0.092, -0.056), resolution=(2520, 1080))))
    sleep()
    touch(v=(350,900)) # 指令卡1
    sleep()
    touch(v=(750,900)) # 指令卡2
    sleep()
    snapshot(msg="弓凛宝具动画")

    touch(wait(Template(r"tpl1576850295381.png", record_pos=(-0.053, 0.168), resolution=(2520, 1080)),timeout=60)) # 从者经验值界面
    touch(wait(Template(r"tpl1576850295381.png", record_pos=(-0.053, 0.168), resolution=(2520, 1080)))) # 御主经验值界面
    touch(wait(Template(r"tpl1576850387830.png", record_pos=(0.225, 0.188), resolution=(2520, 1080)))) # QP界面
