# -*- encoding=utf8 -*-
from airtest.core.api import *
import utils.index as util
import images.index as images
from utils.info import getInfo

LoseMaxNum = 4


def TupoMain():
    global LoseMaxNum
    # 结界突破 StrongholdChallenge
    gs = guideScene()
    if not gs:
        raise Exception("Scene error")
    targetList = find_all(Template(images.get(
        "tupo_target"), threshold=0.9, record_pos=(0, 0), resolution=(2208, 1242)))  # 未挑战
    targetStopList = find_all(Template(images.get(
        "tupo_target_stop"), threshold=0.9, record_pos=(0, 0), resolution=(2208, 1242)))  # 挑战失败
    targetPassList = find_all(Template(images.get(
        "tupo_target_pass"), threshold=0.7, record_pos=(0, 0), resolution=(2340, 1080)))  # 挑战成功
    targetLen = len(targetList) if targetList else 0
    targetStopLen = len(targetStopList) if targetStopList else 0
    targetPassLen = len(targetPassList) if targetPassList else 0
    total = targetLen + targetStopLen + targetPassLen
    backNum = LoseMaxNum - targetPassLen - targetStopLen
    if total != 9:
        backNum = 0
        util.print_(
            "Tupo Error", f"exception! {targetLen}:{targetStopLen}:{targetPassLen}")
    if targetLen > 0:
        for i in range(targetLen):
            attackResult = attackTarget(targetList[i], backNum > 0)
            if attackResult == False:  # 突破券不足
                return TupoEnd()
            elif attackResult == -1 and backNum > 0:
                targetStopLen += 1
                util.log("Tupo", "0")
            elif attackResult == -2:
                TupoMain()
            else:
                util.log("Tupo", "3")
            backNum -= 1
    targetList = find_all(Template(images.get(
        "tupo_target"), threshold=0.9, record_pos=(0, 0), resolution=(2208, 1242)))  # 未挑战
    if targetStopLen > 0 and targetList == None:
        util.findTouch(Template(images.get("tupo_refresh"),
                       record_pos=(0.263, 0.154), resolution=(2340, 1080)))
        util.sleep(1, 0)
        util.waitTouch(Template(images.get("tupo_confirm"),
                       record_pos=(0.091, 0.056), resolution=(2208, 1242)))
        util.sleep(1, 0)
        util.log("Tupo", "R")
    elif targetLen == 0 and total == 8:  # 道馆突破
        return TupoEnd()
    TupoMain()


def attackTarget(target, backAct=False):
    backValue = True
    util.touch((target["result"][0] - 100,
               target["result"][1] + 50))  # 右上角位置偏移了
    util.sleep(1, 0)
    waitfind = util.waitTouch(
        Template(images.get("tupo_attack"), resolution=(2208, 1242)), timeout=10)
    if not waitfind:  # 协作出现打断进程
        util.print_("TupoError", "AttackTarget error")
        util.exceptionSceneHandle()
        return -2
    util.sleep(2)
    entryBtnFind = find_all(
        Template(images.get("tupo_attack"), resolution=(2208, 1242)))
    if entryBtnFind != None:
        util.touch((100, 100))
        util.sleep(1)
        return False
    if backAct:
        util.waitTouch(Template(images.get("fight_back"), threshold=0.83, record_pos=(
            -0.426, -0.209), resolution=(2340, 1080)), timeout=15, touchtime=1.5)
        back_confirm = util.waitTouch(Template(images.get("fight_back_confirm"), record_pos=(
            0.077, 0.049), resolution=(2208, 1242)), timeout=10)
        if back_confirm:
            util.waitTouch(Template(images.get("fight_fail_attack"), record_pos=(
                0.171, 0.113), resolution=(2208, 1242)), timeout=12)
            util.waitTouch(images.getTemplate(
                "fight_fail_attack_confirm"), timeout=10)
            util.sleep(3, 0)
    util.sleep(2, 0)
    outMain = GetOurMain(find_all(images.getm("tupo_our_main")))
    if outMain:
        util.touch(outMain, f=8, offset=(0, 200))
    util.sleep(9)
    # coding + 重写等待结果
    moveBack = util.watchMove(Template(images.get("fight_back"), threshold=0.83, record_pos=(
            -0.426, -0.209), resolution=(2340, 1080)), timeout=300, interval=4)
    if moveBack:
        util.sleep(1, 0)
        failIcon = find_all(Template(images.get(
            "fight_fail"), threshold=0.9, record_pos=(-0.131, -0.147), resolution=(2208, 1242)))
        if failIcon == None:
            util.touch((100, 100))
            util.sleep(1, 0)
            util.touch((100, 100))
            util.sleep(2, 0)
            util.touch((100, 100))
            util.sleep(2, 0)
            successGift = find_all(Template(images.get(
                "tupo_reward"), record_pos=(-0.005, 0.108), resolution=(2340, 1080)))
            if successGift != None:
                util.touch((100, 100))
                util.sleep(1, 0)
                util.touch((100, 100))
                util.sleep(1, 0)
        else:
            backValue = -1
            util.touch((100, 100))
            util.sleep(2, 0)
    mainScene = util.wait(Template(images.get("tupo_head"), record_pos=(
        0.006, -0.169), resolution=(2340, 1080)), timeout=10)
    if mainScene == None:
        raise Exception("Scene error")
    return backValue


def TupoEnd():
    util.findTouch(Template(images.get("tupo_close"), record_pos=(
        0.366, -0.145), resolution=(2340, 1080)))
    util.log("Tupo", "E")
    util.clearLog("Tupo")
    return util.completionTask("Tupo")


def GetOurMain(ls):
    if not ls:
        return None
    value = None
    for item in ls:
        itemv = item["result"]
        if not value:
            value = itemv
        elif itemv[0] < value[0]:
            value = itemv
    return value


def guideScene():
    Scenes = [
        Template(images.get("tansuo"), record_pos=(
            0.027, -0.172), resolution=(2208, 1242)),
        Template(images.get("tupo_entry"),
                 record_pos=(-0.279, 0.177), resolution=(2340, 1080)),
        Template(images.get("tupo_head"), record_pos=(
            0.006, -0.169), resolution=(2340, 1080))
    ]
    isTupoPanel = find_all(Scenes[2])
    value = False
    if isTupoPanel:
        confirmBtn = find_all(Template(images.get("tupo_confirm"), record_pos=(
            0.091, 0.056), resolution=(2208, 1242)))
        if confirmBtn and len(confirmBtn) > 1:
            util.touch(confirmBtn)
        value = True
    else:
        value = util.guideScene(Scenes)
        util.log("Tupo", "S")
    util.changeTeams("Tupo")
    return value


def main():
    global LoseMaxNum
    LoseMaxNum = getInfo("s")["tupoLoseMaxNum"]
    try:
        TupoMain()
    except Exception as e:
        util.print_("Tupo Error", e)
        util.exceptionSceneHandle()
        main()
