# -*- encoding=utf8 -*-
from airtest.core.api import *
import utils.index as util
import images.index as images
from utils.info import getInfo

innerMaxNum = -1


def mainCombat(combatIndex=0, moveScene=0, maxMoveScene=3, miss=0):
    # 探索副本
    boostBoosLoc = None
    boostLoc = None
    if combatIndex > 1 and miss == 0:
        boostBoosLoc = find_all(
            Template(
                images.get("tansuo_monster_boss"),
                threshold=0.8,
                record_pos=(-0.002, -0.07),
                resolution=(2208, 1242),
            )
        )  # boss目标
    if boostBoosLoc == None:
        boostLoc = find_all(
            Template(
                images.get("tansuo_monster"),
                threshold=0.8,
                record_pos=(0.238, -0.06),
                resolution=(2208, 1242),
            )
        )  # 怪物目标
    if boostBoosLoc != None:
        attackTarget(boostBoosLoc, True)
        nextCombat(True)
    elif boostLoc != None:
        attackBack = attackTarget(boostLoc)
        if attackBack:
            combatIndex += 1
        elif attackBack == None:
            miss = 1
        mainCombat(combatIndex, moveScene, miss=miss)
    elif moveScene < maxMoveScene:
        moveSquare()
        mainCombat(combatIndex, moveScene=moveScene + 1)
    else:
        nextCombat()


def nextCombat(isBoss=False):
    global innerMaxNum
    MaxNum = getInfo("s")["tansuoMaxNum"]
    if innerMaxNum > 0:
        MaxNum = innerMaxNum
    combatExit()
    logStr = util.log("Tansuo", False)
    if util.isMaxNum(logStr) > MaxNum:
        util.clearLog("Tansuo")
        util.closeBuff()  # 退出加成
        return util.completionTask("Tansuo")
    else:
        sc = guideScene(2 if isBoss else 0)
        sc and mainCombat()


missTarget = 0


def attackTarget(coord, isBoss=False):
    global missTarget
    # 怪物异常
    if missTarget > 4:
        missTarget = 0
        util.print_("Fix target max misses")
        return util.exceptionSceneHandle(False)
    # 探索内，攻击目标
    util.touch(coord, 30 if isBoss else 1)
    util.sleep(1)
    if isCenter() != None:
        util.print_("Target click miss")  # 未命中，需要异常处理
        missTarget += 1
        return None
    try:
        util.sleep(5)
        util.waitTouch(
            Template(
                images.get("fight_success"),
                record_pos=(-0.091, -0.15),
                resolution=(2532, 1170),
            )
        )
        rewardBack = util.wait(
            Template(
                images.get("fight_reward"),
                record_pos=(-0.022, 0.139),
                resolution=(2208, 1242),
            )
        )
        if rewardBack:
            util.moveTouch(
                Template(
                    images.get("fight_reward"),
                    record_pos=(-0.022, 0.139),
                    resolution=(2208, 1242),
                ),
                f=8,
            )
    except TargetNotFoundError:
        missTarget += 1
        util.print_("Tansuo Error", "End game error iden")
        return None
    util.wait(
        Template(
            images.get("tansuo_iden"),
            record_pos=(0.134, 0.239),
            resolution=(2208, 1242),
        ),
        timeout=5,
    )
    if isBoss:
        util.sleep(2)
    # marks number
    util.log("Tansuo", "2" if isBoss else "1")
    missTarget = 0
    return True


def isCenter():
    shishenlu = find_all(
        Template(
            images.get("tansuo_iden"),
            record_pos=(0.134, 0.239),
            resolution=(2208, 1242),
        )
    )
    lunhuan = find_all(images.getm("tansuo_iden_lunhuan"))
    return lunhuan and shishenlu  # 式神录，是否为查找场景


def moveSquare():
    center = isCenter()
    if center == None:
        return False
    centerCoord = center[0]["result"]
    centerCoordNew = (centerCoord[0], 200)
    util.swipe(centerCoordNew, (centerCoord[0] - 800, 200), duration = 1)
    return True


def combatExit():
    # 探索结束退出
    reslutCoord = True
    hasReslut = False
    util.sleep(1)
    maxLoop = 4
    while reslutCoord != None and maxLoop > 0:
        maxLoop -= 1
        reslutCoord = find_all(
            Template(
                images.get("tansuo_reward"),
                threshold=0.75,
                record_pos=(-0.065, 0.082),
                resolution=(2340, 1080),
            )
        )  # 通关小盒子
        if reslutCoord != None:
            hasReslut = True
            for item in reslutCoord:
                util.log("Tansuo", "G")
                util.touch(item)
                util.sleep(0.5)
                util.touch((300, 100))
                util.sleep(0.5)
            util.sleep(1)
    hasReslut and util.sleep(1)
    util.log("Tansuo", "E")
    if isCenter():
        util.findTouch(
            Template(
                images.get("tansuo_back"),
                record_pos=(-0.412, -0.191),
                resolution=(2340, 1080),
            )
        )  # 返回按钮
        util.waitTouch(
            Template(
                images.get("tansuo_back_confirm"),
                record_pos=(0.087, 0.027),
                resolution=(2340, 1080),
            )
        )  # 确认按钮
        util.log("Tansuo", "B")
    giftIcon = find_all(
        Template(
            images.get("tansuo_reward_box"),
            threshold=0.8,
            record_pos=(0.069, -0.09),
            resolution=(2208, 1242),
        )
    )
    if giftIcon:
        util.touch(giftIcon)
        giftBack = util.wait(
            Template(
                images.get("fight_reward"),
                record_pos=(-0.022, 0.139),
                resolution=(2208, 1242),
            )
        )
        util.touch(giftBack)
        util.log("Tansuo", "g")
    util.sleep(1)


def guideScene(level=0):
    global firstAction
    Scenes = [
        Template(
            images.get("tansuo"), record_pos=(0.027, -0.172), resolution=(2208, 1242)
        ),
        Template(
            images.get("tansuo_entry"),
            threshold=0.85,
            record_pos=(0.371, 0.136),
            resolution=(2340, 1080),
        ),
        Template(
            images.get("tansuo_entry_2"),
            threshold=0.8,
            record_pos=(0.195, 0.113),
            resolution=(2340, 1080),
        ),
        images.getm("tansuo_iden_lunhuan"),
    ]
    value = util.guideScene(Scenes, level)
    if value == None:
        return fixInnerScene(Scenes)
    if value and firstAction:
        util.changeTeams("Tansuo")
        firstAction = False
    util.log("Tansuo", "S")
    return value


def fixInnerScene(Scenes):
    # 业务内部场景修复
    icon = find_all(
        Template(
            images.get("fight_reward"),
            threshold=0.85,
            record_pos=(-0.45, 0.191),
            resolution=(2340, 1080),
        )
    )
    if icon:
        util.touch(icon)
        util.sleep(1)
    util.log("Tansuo", "s")
    return util.guideScene(Scenes)


firstAction = True


def main(maxNum=-1):
    global firstAction
    global innerMaxNum
    firstAction = True
    innerMaxNum = maxNum
    guideScene()
    util.openBuff()
    mainCombat()
