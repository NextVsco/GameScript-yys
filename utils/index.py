import random
import time
from airtest.core.api import *
from airtest.core.helper import G
import images.index as images
import re

from utils.info import getInfo


def touchArea(area, f=30, offset=(0, 0)):  # 区域点击方形
    if len(area) < 4:
        G.DEVICE.touch(shakeArea(area, f, offset))
        return True
    start = area[0]
    end = area[2]
    x = end[0] - start[0]
    y = end[1] - start[1]
    x = float(format(random.random() * x, ".2f"))
    y = float(format(random.random() * y, ".2f"))
    result = (start[0] + x + offset[0], start[1] + y + offset[1])
    G.DEVICE.touch(result)
    return True


def shakeArea(loc, f=30, offset=(0, 0)):  # 中点抖动
    basenum = f
    loc1 = loc[0] + offset[0]
    +float(format(random.random() * basenum - basenum / 2, ".2f"))
    loc2 = loc[1] + offset[1]
    +float(format(random.random() * basenum - basenum / 2, ".2f"))
    return (loc1, loc2)


def touch(e, f=30, offset=(0, 0)):
    global SceneRepair
    if SceneRepair:
        print_("Error", "Scene repair, Fixing")
        SceneRepair = False
        exceptionSceneHandle()
    # find_all callback compatible
    if type(e).__name__ == "list" and type(e[0]).__name__ == "dict":
        return touchArea(e[0]["result"], f, offset)
    elif type(e).__name__ == "dict":
        return touchArea(e["result"], f, offset)
    elif type(e).__name__ == "tuple":
        return touchArea(e, f, offset)
    else:
        print_("Error", "Unit touch type error", e)
        return None


def findTouch(v, f=30, offset=(0, 0)):
    targets = find_all(v)
    return touch(targets, f, offset) if targets else False


def waitTouch(v, interval=0.8, timeout=12, f=30, offset=(0, 0), touchtime=0):
    tarloc = wait(v, timeout=timeout, interval=interval)
    if tarloc and touchtime > 0:
        sleep(touchtime)
        tarloc = wait(v, timeout=timeout, interval=interval)
    return touch(tarloc, f, offset)


def moveTouch(v, f=30, max=5, sleeptime=0, offset=(0, 0)):
    targets = find_all(v)
    if targets:
        touch(targets, f, offset)
        if sleeptime > 0:
            sleep(sleeptime)
        return moveTouch(v, f, max=max - 1, sleeptime=sleeptime, offset=offset)
    else:
        return True


isIOS = False  # ios 屏幕横左右有问题！（头向左👈）
linkUrl = ""


def isIOSsys():
    global isIOS
    return isIOS


def connectDevice(url):
    global isIOS
    global linkUrl
    if url:
        linkUrl = url
    elif not url and linkUrl:
        url = linkUrl
    isIOS = "ios" in url
    print_(None, f"isIOS:{isIOS} {linkUrl}")
    return connect_device(url)


def swiperAuto(v, len, **kwargs):
    global isIOS
    newLoc = shakeArea(v)
    if isIOS:
        len = (len[0] * 2, len[1] * 2)
    targetLoc = (
        newLoc[0] + randomShake(len[0], 100),
        newLoc[1] + randomShake(len[1], 100),
    )
    if not isIOS:
        G.DEVICE.swipe(newLoc, targetLoc, **kwargs)
    else:
        G.DEVICE.swipe((newLoc[1], newLoc[0]), (targetLoc[1], targetLoc[0]), **kwargs)
    sleep(0.5)


def swiper(d="l"):
    if d == "l":
        return G.DEVICE.swipe((282, randomShake(450, 50)), (142, 0))
    elif d == "images.get(":
        return G.DEVICE.swipe((282, 0), (142, randomShake(450, 50)))


def swipe_(v1, v2, vector=None, duration=0.5, **kwargs):
    return swipe(v1, v2, vector, duration, **kwargs)


def randomShake(num, f):
    return float(format(random.random() * f - f / 2 + num, ".2f"))


def sleepAuto(t, f=0.25):
    if f == 0 or t <= 1:
        return time.sleep(t)
    return time.sleep(randomShake(t + 0.25, 0.5))


sleep = sleepAuto


def watchMove(v, timeout=20, interval=2):
    if interval < 2:
        interval = 2
    if timeout > 1:
        try:
            timeout -= interval
            targets = find_all(v)
            if targets == None:
                return True
            else:
                sleep(interval - 0.9)
                return watchMove(v, timeout)
        except TargetNotFoundError:
            return True
    return False


def wait(v, timeout=10, interval=2, touchtime=0, more=False):
    if timeout > 1 or timeout == -1:
        timeStart = time.time()
        targets = find_all(v)
        timeSleep = time.time() - timeStart
        if timeout != -1:
            timeout -= interval if interval > 0 else timeSleep
        if targets != None:
            if touchtime > 0:
                sleep(touchtime, 0)
                targets = find_all(v) or targets
            if more:
                return targets
            return targets[0]["result"]
        else:
            if timeSleep < interval:
                sleep(interval - timeSleep)
            return wait(v, timeout, interval, touchtime, more)
    print_(None, "Wait not", v)
    return None


"""
阴阳师业务方法
"""


SceneRepair = False


def guideScene(Scenes, again=False, level=0):
    # [code] 从level开始查找，倒序
    findT = True
    index = len(Scenes)
    maximize = index * 2
    value = None
    while index > 0 and maximize > 0:
        maximize -= 1
        nowIndex = index - 1
        if findT:
            value = find_all(Scenes[nowIndex])
            if value == None:
                index -= 1
            else:
                if index == len(Scenes):
                    break
                else:
                    touch(value)
                    findT = False
                    index += 1
        else:
            target = wait(Scenes[nowIndex], timeout=10)
            if index != len(Scenes):
                touch(target)
                index += 1
            else:
                break
    if maximize < 0:
        print_("Message", "Scene find error,in loop")
        return None
    if value == None and again == False:
        return exceptionSceneHandle(Scenes)
    print_(
        "Message", "Fixing the scene" if again == False else "Fixing the scene again"
    )
    return value


def exceptionSceneHandle(Scenes=None):
    print_("Message", "Agin scene search start.")
    exits = [
        Template(
            images.get("tupo_close"),
            threshold=0.8,
            record_pos=(0.366, -0.145),
            resolution=(2340, 1080),
        ),  # 右上角关闭
        Template(
            images.get("fight_back_confirm"),
            record_pos=(0.091, 0.056),
            resolution=(2208, 1242),
        ),
        Template(
            images.get("other_confirm"),
            record_pos=(0.093, 0.054),
            resolution=(2208, 1242),
        ),
        Template(
            images.get("xiezuo_refuse"),
            threshold=0.85,
            record_pos=(0.137, 0.1),
            resolution=(2340, 1080),
        ),  # 关闭（拒接）
        Template(
            images.get("xiezuo_close"),
            threshold=0.85,
            record_pos=(0.442, -0.179),
            resolution=(2208, 1242),
        ),  # 关闭
        Template(
            images.get("msg_retract"),
            threshold=0.85,
            record_pos=(0.013, -0.004),
            resolution=(2208, 1242),
        ),  # 聊天收起
        Template(
            images.get("fight_reward"),
            threshold=0.85,
            record_pos=(-0.022, 0.139),
            resolution=(2208, 1242),
        ),  # 战斗结束奖励
        Template(
            images.get("fight_fail"),
            threshold=0.85,
            record_pos=(-0.022, 0.139),
            resolution=(2208, 1242),
        ),  # 战斗失败
        Template(
            images.get("tansuo_back"),
            threshold=0.85,
            record_pos=(-0.474, -0.254),
            resolution=(2208, 1242),
        ),  # 后退
        Template(
            images.get("tansuo_back_confirm"),
            threshold=0.85,
            record_pos=(0.087, 0.027),
            resolution=(2340, 1080),
        ),  # 确认后退
        Template(
            images.get("close"),
            threshold=0.85,
            record_pos=(0.114, -0.181),
            resolution=(2208, 1242),
        ),  # 取消
    ]
    clickScene = True
    for exitItem in exits:
        exitBtn = find_all(exitItem)
        if exitBtn:
            clickScene = False
            touch(exitBtn)
            sleep(1)
    # tansuo coding
    if clickScene:
        touch((100, 300))
        sleep(1)
    log(value="Ê")
    if Scenes:
        return guideScene(Scenes, again=True)
    return False


openBuffState = False  # [C]加成控制状态


def openBuff():  # 打开加成
    global openBuffState
    openBuffState = getInfo("s")["openBuffState"]
    if not openBuffState:
        return False
    sleep(1, 0)
    buffEntry = find_all(
        Template(
            images.get("buff_entry"),
            record_pos=(-0.003, -0.249),
            resolution=(2208, 1242),
        )
    )
    touch(buffEntry)
    sleep(1, 0)
    openbtns = find_all(
        Template(
            images.get("buff_open"),
            threshold=0.8,
            record_pos=(0.183, -0.002),
            resolution=(2208, 1242),
        )
    )
    if openbtns != None:
        exps = find_all(
            Template(
                images.get("buff_exp"),
                record_pos=(-0.188, -0.001),
                resolution=(2208, 1242),
            )
        )
        for exp in exps:
            for open_item in openbtns:
                exp_target = exp["result"][1]
                open_target = open_item["result"][1]
                if abs(exp_target - open_target) < 10:
                    touch(open_item, f=10)
                    sleep(0.5, 0)
        sleep(1, 0)
    touch(buffEntry)
    sleep(1, 0)


def closeBuff():  # 关闭加成
    global openBuffState
    if not openBuffState:
        return False
    sleep(1, 0)
    buffEntry = find_all(
        Template(
            images.get("buff_entry"),
            record_pos=(-0.003, -0.249),
            resolution=(2208, 1242),
        )
    )
    touch(buffEntry)
    sleep(0.5, 0)
    open_buffs = find_all(
        Template(
            images.get("buff_state_open"),
            threshold=0.8,
            rgb=False,
            record_pos=(0.109, -0.055),
            resolution=(2208, 1242),
        )
    )
    if open_buffs != None:
        for open_buff in open_buffs:
            touch(open_buff, f=10)
            sleep(0.5, 0)
        sleep(0.5, 0)
    touch(buffEntry)
    sleep(1, 0)


def expeditedRepair():
    global SceneRepair
    SceneRepair = True


completionTaskState = None


def completionTask(key):
    global completionTaskState
    completionTaskState = key
    print("当前任务完成", key)


def getCompletionTaskState():
    global completionTaskState
    return completionTaskState


logMap = {}
nowKey = "Sys"


def log(key="Sys", value=""):
    global logMap
    global nowKey
    if not key in logMap:
        logMap[key] = ""
    if value:
        nowKey = key
        logMap[key] += value
        _value = logMap[key]
        if len(_value) > 100:
            _value = "..." + _value[len(_value) - 100 :]
        print_(key, f"L{isMaxNum(logMap[key])}", _value)
    return logMap[key]


def clearLog(key):
    global logMap
    if key in logMap:
        logMap[key] = ""
        print_("Sys", f'Clear log "{key}"')


def getLog():
    global logMap
    global nowKey
    if nowKey == "" or not nowKey in logMap:
        return ""
    return logMap[nowKey]


lastTeam = None


def changeTeams(key="tupo", temp=False):
    global lastTeam
    _back = False
    _keyname = "Shishenlu"
    teamLoc = getInfo()["base"]["shishenluTeam"]
    if key.lower() in teamLoc:
        teamLoc = teamLoc[key.lower()]
    else:
        print_(_keyname, f"Please configure the {key} team")
        _back = True
    if teamLoc == lastTeam:
        _back = True
    lastTeam = teamLoc
    if not _back:
        entry = find_all(images.getm("team_entry"))
        if not entry:
            entry = find_all(Template(images.get("tansuo_iden"), record_pos=(0.134, 0.239), resolution=(2208, 1242)))
        if entry:
            touch(entry)
            sleep(1)
        isShishenlu = find_all(images.getm("team_shishenlu"))
        if isShishenlu:
            waitTouch(images.getm("team_yushe"), touchtime=0.5)
            sleep(1)
            teamGroups = find_all(images.getm("team_group"))
            teamGroups = sorted(teamGroups, key=lambda x: x["result"][1])
            if teamLoc:
                teamLoc = [int(x) - 1 for x in teamLoc.split(",")]
                touch(teamGroups[teamLoc[0]])
                sleep(1)
                teamGroupsUse = find_all(images.getm("team_group2"))
                teamGroupsUse = sorted(teamGroupsUse, key=lambda x: x["result"][1])
                touch(teamGroupsUse[teamLoc[1]])
                sleep(1.5)
                isConfirm = findTouch(
                    Template(
                        images.get("other_confirm"),
                        record_pos=(0.093, 0.054),
                        resolution=(2208, 1242),
                    )
                )
                if isConfirm:
                    sleep(1)
        findTouch(images.getm("team_back"))
    sleep(1)


"""
Other
"""


def getTime():
    return time.strftime("%H:%M:%S")


def isMaxNum(str):
    value = re.sub("[^0-9]", "", str)
    return len(value) if value else 0


# 输出控制台信息
def print_(key, msg="NULL", *msgs):
    global nowKey
    if not key:
        key = nowKey
    keyText = f"\x1b[1;33m[{key}]\x1b[0m"
    timeText = f"\x1b[1;32m{getTime()}\x1b[0m"
    print(f"{keyText} {timeText} {msg}", *msgs)
