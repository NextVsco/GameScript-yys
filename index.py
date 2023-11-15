from airtest.core.api import *
import Dungeon_Tupo.index as tupo
import Dungeon_Tansuo.index as tansuo
import Dungeon_Other.index as other
import Dungeon_Liudao.index as liudao

import Dungeon_Yuhun_Group.index as yuhun
import utils.watcher as watcher
import utils.index as util
import utils.info as info
import images.index as images


actionIndex = 0


def loopAction():
    global actionIndex
    infodata = info.getInfo()
    scene = infodata["task"]["scene"]
    if actionIndex >= len(scene):
        actionIndex = actionIndex % len(scene)
    scenekey = str(scene[actionIndex])
    if scenekey.lower() == "tupo":
        tupo.main()
    elif scenekey.lower() == "tansuo":
        tansuo.main()
    elif scenekey.lower() == "yuling":
        other.action(time=12, type="yuling")
    elif scenekey.lower() == "act":
        other.action(time=7)
    elif scenekey.lower() == "actm":
        other.actionM()
    elif scenekey.lower() == "liudao":
        liudao.main()
    elif scenekey.lower() == "yuhunh":
        yuhun.mainYuhun(attackNum=34, header=True)
    elif scenekey.lower() == "yuhun":
        yuhun.mainYuhun(attackNum=34)
    completionTaskState = util.getCompletionTaskState()
    if completionTaskState and str(completionTaskState).lower() == scenekey.lower():
        actionIndex += 1


def main():
    infodata = info.getInfo()
    equipments = infodata["equipment"]
    if not equipments or not len(equipments):
        return util.print_(None, "Configure the device address, Please")
    equipmentState = infodata["equipmentState"]
    linkurl = None
    linkindex = None
    for index, item in enumerate(equipmentState):
        if item == None or not item["link"]:
            linkurl = equipments[index]
            linkindex = index
            # info.setInfo({f"equipmentState.${index}": {"link": True}})
            break
    if linkurl:
        arrangeWork(linkurl, linkindex)
    else:
        print("No more equipment")
    infodata = None


def arrangeWork(url, index):
    util.connectDevice(url)
    watcher.main()
    loopTask = not info.getInfo("s")["close"]
    lastTime = None
    # TEST POINT
    while loopTask:
        try:
            lastTime = time.time()
            loopAction()
        except Exception as e:
            nowTime = time.time()
            util.print_(None, "异常结束XOOOOOOOOOOOOOX")
            print(e)
            if nowTime - lastTime < 20:
                util.exceptionSceneHandle()
                sleep(5)
        loopTask = not info.getInfo("s")["close"]
    watcher.close()
    info.setInfo({f"equipmentState.${index}": {"link": False}})
    info.close()


main()