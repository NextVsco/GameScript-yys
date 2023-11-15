# -*- encoding=utf8 -*-

from airtest.core.api import *
import utils.index as util
import images.index as images


def main(type="tu"):
    entrance(type)


def mainTu():  # 魂土，御魂-悲鸣
    entrance("tu")


def mainWang():  # 魂王，御魂神罚·贰
    entrance("wang")


def entrance(type):
    sceneTarget = find_all(images.getm("yuhun_ident"))
    if sceneTarget == None:
        guideScene()
    # 八岐大蛇
    if type == "tu":
        # 选择悲鸣
        util.touch(images.getm("yuhun_entry_tu"))
    elif type == "wang":
        # 选择神罚
        util.touch(images.getm("yuhun_entry_tu"))

    # 挑战/组队
    # 式神录 - 配置阵容
    teamChange("SN")
    # 打开加成
    # 循环挑战

def guideScene():
    Scenes = [
        Template(images.get("tansuo"), record_pos=(0.027, -0.172), resolution=(2208, 1242)),
        images.getm("yuhun_entry"),
        images.getm("yuhun_entry2"),
        images.getm("yuhun_ident")
    ]
    value = util.guideScene(Scenes)
    util.log("Yuhun", "S")
    return value


def teamChange(type):
    print("Team change")
    util.sleep(30)


# mainTu()
def temp():
    util.wait(
        Template(
            r"tpl1680787391289.png",
            threshold=0.85,
            record_pos=(-0.45, 0.191),
            resolution=(2340, 1080),
        ),
        timeout=120,
    )
    util.sleep(1)
    util.util.touch((100, 150))
    util.sleep(1)
    util.util.touch((100, 150))
    util.sleep(1)
    util.util.touch((100, 150))
    iconIden = find_all(
        Template(
            r"tpl1680787391289.png",
            threshold=0.85,
            record_pos=(-0.45, 0.191),
            resolution=(2340, 1080),
        )
    )
    if iconIden != None:
        sleep(2)
        util.util.touch((100, 150))
    util.sleep(30)
    temp()



actionEntry = False # 是否活动
groupMain = False # 是否队长
groupMax = False # 是否满队员
def mainYuhun(attackNum=60, time=20, header=False):  # 爬塔活动
    global groupMain 
    global groupMax 
    global actionEntry 
    start = None
    if groupMain or header:
        # yuhun group
        entry_info = Template(images.get("yuhun_group_entry"), record_pos=(0.408, 0.176), resolution=(2532, 1170))
        start = util.wait(entry_info)
        if start:
            if groupMax:
                util.watchMove(images.getm("yuhun_group_team"))
            util.moveTouch(entry_info, max=10, sleeptime=2)
    if actionEntry:
        util.sleep(2.5)
        util.wait(Template(images.get("tansuo_back"), threshold=0.7, record_pos=(-0.474, -0.254), resolution=(2208, 1242)))
        util.touch((2200,1000))
    # Start action.
    if start or not groupMain:
        util.sleep(time + 1)
        util.waitTouch(Template(images.get("fight_success"), record_pos=(
            -0.091, -0.15), resolution=(2532, 1170)), timeout=(time+1)*2)
        rewardBack = util.wait(Template(images.get("fight_reward"),
                                        record_pos=(-0.022, 0.139), resolution=(2208, 1242)), timeout=time*2)
        if rewardBack:
            util.sleep(2, 0)
            util.moveTouch(Template(images.get("fight_reward"),record_pos=(-0.022, 0.139), resolution=(2208, 1242)))
            util.log("Other", "4")
    else:
        util.touch((100, 100))
    mainYuhun(attackNum=attackNum-1, time=time, header=header)
