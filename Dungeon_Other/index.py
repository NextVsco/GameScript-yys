from airtest.core.api import *
import utils.index as util
import images.index as images


def action(attackNum=1000, time=20, first=True, errnum=3, type=None):  # 爬塔活动
    entryTimeout = 3 if errnum >= 3 else 12
    entryBack = None
    if type == None:
        entryBack = util.waitTouch(images.getm("action_entry"), timeout=entryTimeout)
    elif type == "yuling":
        entryBack = util.waitTouch(images.getm("other_yuling_entry"), timeout=entryTimeout)
    fightBack = None
    if first:
        util.log("Other", "F")
    if entryBack:
        util.sleep(time + 1)
        if type == "yuling":
            fightBack = util.waitTouch(
                images.getm("fight_reward"),
                timeout=time * 2,
                touchtime=1,
                offset=(-300, 0),
            )
        else:
            fightBack = util.waitTouch(
                images.getm("action_fight_success"),
                timeout=time * 2,
                touchtime=1,
                offset=(-300, 0),
            )
        util.sleep(0.5)
        util.touch((100, 200))
        util.sleep(1)
        util.touch((100, 200))
        if fightBack:
            errnum = 0
            util.log("Other", "4")
    else:
        if errnum >= 3:
            guideScene()
        else:
            errnum += 1
            util.touch((100, 300))
    if attackNum > 0:
        action(attackNum - 1, time=time, first=False, errnum=errnum, type=type)


def guideScene():
    Scenes = [
        images.getm("action_entry1"),
        images.getm("action_entry2"),
        images.getm("action_entry3"),
        images.getm("action_entry"),
    ]
    value = util.guideScene(Scenes)
    util.log("Other", "S")
    if value:
        util.changeTeams("action")
    return value


# 活动-破晓时分
buffNum = None
yiwuNum = None
buffWaitNum = None


def actionM():
    global buffNum
    global yiwuNum
    global buffWaitNum
    entryback = util.waitTouch(images.getm("action_px_entry"), timeout=6)
    buffWaitNum = 0
    if entryback:
        buffNum = 0
        yiwuNum = 0
        util.waitTouch(images.getm("action_px_btn_choose"))
        sleep(1)
        actionMChooseTeam()
        util.log("Actm", "T" + str(buffNum))
    else:
        buffNum = 5 if buffNum == None else buffNum
        yiwuNum = 5 if yiwuNum == None else yiwuNum
        shishenChoose = find_all(images.getm("action_px_choose_shishen"))
        if shishenChoose:
            actionMChooseTeam(sup=True)
        else:
            util.touch((100, 300))
            util.sleep(1)
    actionMChooseEvent()
    return print("End of event actionM~")


def actionMChooseTeam(maxNum=5, sup=False):
    global buffNum
    maxNum -= 1
    util.sleep(1)
    # 式神选择排序，选择带有buff的式神
    shishenBtns = find_all(images.getm("action_px_choose_shishen"))
    if shishenBtns == None:
        return False
    buffs = find_all(images.getm("action_px_buff"))
    shishenLineY = find_all(images.getm("action_px_shishen_line"))[0]["result"][1]
    shishenBtns = sorted(shishenBtns, key=lambda x: x["result"][0])
    if buffs:
        buffs = [i for i in buffs if i["result"][1] > shishenLineY]
    if buffs:
        if not sup:
            buffNum += 1
        buffTarget = buffs[0]
        for btn in shishenBtns:
            if buffTarget["result"][0] < btn["result"][0]:
                util.touch(btn)
                break
    else:
        util.touch(shishenBtns)
    if maxNum <= 0:
        return True
    return actionMChooseTeam(maxNum, sup)


def actionMChooseEvent():
    global buffNum
    global buffWaitNum
    events = [
        "action_px_icon_yiwu",
        "action_px_icon_qiyu",
        "action_px_icon_store",
        "action_px_icon_suiji",
        "action_px_icon_yingzhan",
        "action_px_icon_liudao",
        "action_px_icon_boss",
    ]
    for _ in range(26):
        _key = None
        for index, key in enumerate(events):
            if buffNum < 5:
                if index == 0:
                    key = events[4]
                elif index == 4:
                    key = events[0]
            target = find_all(images.getm(key))
            if target:
                util.touch(target)
                _key = key
                actionMEventAction(key)
                break
        if _key == None:
            actionMEventAction("action_px_icon_suiji")
        if _key == "action_px_icon_boss":
            util.clearLog("Actm")
            break


def actionMEventAction(key):
    global buffNum
    global yiwuNum
    global buffWaitNum
    match key:
        case "action_px_icon_yiwu":
            if yiwuNum < 5:
                util.wait(images.getm("action_px_move"))
                yiwuTarget = find_all(images.getm("action_px_yiwu_iden2"))[0]
                chooseBtns = find_all(images.getm("action_px_btn_choose"))
                for btn in chooseBtns:
                    if abs(yiwuTarget["result"][0] - btn["result"][0]) < 300:
                        util.touch(btn)
                        continue
                yiwuNum += 1
                util.waitTouch(images.getm("action_px_success_huode"))
            else:
                util.waitTouch(images.getm("action_px_move"))
                util.waitTouch(images.getm("action_px_success_huode"))
        case "action_px_icon_qiyu":
            util.sleep(2)
            util.waitTouch(images.getm("action_px_move_back"), touchtime=2, f=10)
            util.waitTouch(images.getm("action_px_success_huode"))
        case "action_px_icon_store":
            util.sleep(2)
            util.waitTouch(images.getm("action_px_move_back"), touchtime=2, f=10)
            util.waitTouch(images.getm("action_px_success_huode"))
        case "action_px_icon_yingzhan":
            if buffWaitNum > 0 and yiwuNum < 5:
                util.wait(images.getm("action_px_zhunbei"))
                changeTeamBuff()
            util.waitTouch(images.getm("action_px_zhunbei"))
            util.waitTouch(images.getm("action_px_success_shengli"), timeout=120)
            util.wait(images.getm("action_px_move"))
            buffTarget = find_all(images.getm("action_px_buff2"))
            if (buffNum + buffWaitNum) < 5 and buffTarget:
                util.findTouch(images.getm("action_px_buff2"), offset=(-100, 20))
                util.sleep(1)
                util.findTouch(images.getm("action_px_btn_jinghua"))
                util.waitTouch(images.getm("action_px_success_huode"))
                buffWaitNum += 1
            else:
                util.waitTouch(images.getm("action_px_move"))
                util.waitTouch(images.getm("action_px_success_huode"))
        case "action_px_icon_liudao":
            util.waitTouch(images.getm("action_px_zhunbei"))
            util.sleep(12)
            liudao = util.waitTouch(images.getm("action_px_success_shengli"), timeout=100)
            util.log("Actm", "2")
            if liudao == None:
                util.waitTouch(images.getm("action_px_success_shengli"), timeout=100)
            util.sleep(3)
            util.waitTouch(images.getm("action_px_move_back"), f=10, timeout=24)
            util.waitTouch(images.getm("action_px_success_huode"))
        case "action_px_icon_boss":
            util.sleep(2)
            util.waitTouch(images.getm("action_px_boss_attack"), f=10)
            util.waitTouch(images.getm("action_px_zhunbei"))
            util.sleep(40)
            util.log("Actm", "2")
            backBoss = util.waitTouch(images.getm("action_px_success_shengli"), timeout=100)
            util.log("Actm", "2")
            if backBoss == None:
                backBoss = util.waitTouch(images.getm("action_px_success_shengli"), timeout=100)
            if backBoss == None:
                backBoss = util.waitTouch(images.getm("action_px_success_shengli"), timeout=100)
            util.sleep(3)
            util.waitTouch(images.getm("action_px_boss_gift"), offset=(-200, 0))
            util.sleep(2)
            util.touch((100, 300))
        case "action_px_icon_suiji":
            util.sleep(8)
            zhunbei = find_all(images.getm("action_px_zhunbei"))
            if zhunbei:
                actionMEventAction("action_px_icon_yingzhan")
            move = find_all(images.getm("action_px_move"))
            moveback = find_all(images.getm("action_px_move_back"))
            move = move or moveback
            if move:
                util.touch(move, f=10)
                util.waitTouch(images.getm("action_px_success_huode"))
            if not move and not zhunbei:
                raise ValueError("No corresponding event!")
        case _:
            raise ValueError("Error actionMEventAction!")
    util.log("Actm", "1")
    util.sleep(1)


def changeTeamBuff(_df=10):
    global buffNum
    global buffWaitNum
    util.wait(images.getm("action_px_user"))
    util.sleep(2)
    util.moveTouch(images.getm("action_px_user"), offset=(-350, -100), f=10)
    util.sleep(4)
    zhandouUsers = find_all(images.getm("action_px_iden_zhandou"))
    zhandouUsers = sorted(zhandouUsers, key=lambda x: x["result"][0])
    buffs = find_all(images.getm("action_px_buff2"))
    nbuffs = find_all(images.getm("action_px_buff"))
    targetLoc = [x for x in nbuffs if x["result"][1] < zhandouUsers[0]["result"][1]]
    targetLoc = sorted(targetLoc, key=lambda x: -x["result"][1])
    targetLoc = targetLoc[0]["result"]
    targetLoc = (targetLoc[0] - 100, targetLoc[1])
    buffs = [x for x in buffs if x["result"][1] > zhandouUsers[0]["result"][1]]
    buffs = sorted(buffs, key=lambda x: x["result"][0])
    zhandouUsersBuff = [0 for _ in range(len(zhandouUsers))]
    minLen = None
    for i, x in enumerate(zhandouUsers):
        _x = x["result"][0]
        for y in buffs:
            _y = y["result"][0]
            _value = abs(_x - _y)
            if minLen == None:
                minLen = _value
                zhandouUsersBuff[i] = _value
            elif zhandouUsersBuff[i] == 0 or abs(_value) < zhandouUsersBuff[i]:
                zhandouUsersBuff[i] = _value
                if _value < minLen:
                    minLen = _value
            elif abs(_y - _x) > minLen:
                break
    waitIndex = 0
    waitUsers = []
    for x in buffs:
        _len = None
        _x = x["result"][0]
        for y in zhandouUsers:
            _y = y["result"][0]
            _value = abs(_x - _y)
            if _len == None:
                _len = _value
            elif _value - _len > _df:
                break
            elif _value - _len < _df:
                _len = _value
        if (_len - minLen) > _df:
            waitUsers.append(x)
    for i, x in enumerate(zhandouUsersBuff):
        if abs(x - minLen) > _df:
            swipe(
                (zhandouUsers[i]["result"][0], zhandouUsers[i]["result"][1] + 100),
                (targetLoc[0], targetLoc[1] - 150),
                duration=1.5,
            )
            util.sleep(3)
            swipe(
                (
                    waitUsers[waitIndex]["result"][0],
                    waitUsers[waitIndex]["result"][1] - 100,
                ),
                (targetLoc[0], targetLoc[1] - 150),
                duration=1.5,
            )
            waitIndex += 1
            buffNum += 1
            buffWaitNum -= 1
            util.sleep(3)
            if buffWaitNum <= 0 or buffNum >= 5:
                break
    util.sleep(0.5)
