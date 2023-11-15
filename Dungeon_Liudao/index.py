from airtest.core.api import *
import utils.index as util
import images.index as images


def main():
    return quickPass()


keyName = "liudao"


def rookieLoop():
    global keyName
    util.waitTouch(images.getm("liudao,entry"))
    util.waitTouch(images.getm("liudao,entry_confirm"))
    util.waitTouch(images.getm("liudao,entry"))
    util.waitTouch(getImage("pop_btn_confirm"))
    util.waitTouch(images.getm("liudao,btn_confirm"))
    util.waitTouch(images.getm("liudao,btn_confirm_b"))
    zhandou = util.waitTouch(images.getm("liudao,guanka_aozhan"), touchtime=2)
    if zhandou:
        util.waitTouch(images.getm("liudao,attack_iden"), offset=(140, 140))
        util.waitTouch(images.getm("liudao,entry_attack"))
        util.log(keyName, "0")
        util.wait(images.getm("liudao,btn_confirm_b"), timeout=100)
        btns = find_all(images.getm("liudao,btn_confirm_b"))
        btns = sorted(btns, key=lambda x: x["result"][0])
        util.touch(btns)
        data = util.waitTouch(images.getm("liudao,success_gift"), touchtime=1)
        if data:
            util.log(keyName, "1")
    util.waitTouch(images.getm("liudao,back"), touchtime=2)
    util.waitTouch(images.getm("liudao,back_confirm"))
    util.waitTouch(getImage("pop_btn_confirm2"))
    util.sleep(3)
    blockTouch(4)
    return rookieLoop()


def blockTouch(num):
    while num:
        util.sleep(1)
        util.touch((100, 300))
        num -= 1
    return None


def getImage(key):
    data = {
        "pop_btn_confirm": Template(
            images.get("fight_back_confirm"),
            record_pos=(0.093, 0.054),
            resolution=(2208, 1242),
        ),
        "pop_btn_confirm2": Template(
            images.get("other_confirm"),
            record_pos=(0.093, 0.054),
            resolution=(2208, 1242),
        ),
    }
    return data[key]


# 椒图速通

firstAction = True
attackNum = 0
buffNum = 0


def quickPass():
    entryEvent()
    _value = chooseEvent()
    if not _value:
        fixScene()
    chooseEvent()
    return


def entryEvent():
    global attackNum
    global buffNum
    entry = util.wait(images.getm("liudao,wanfaxiangqing"), timeout=4)
    if entry:
        attackNum = 0
        buffNum = 0
        util.touch(entry, offset=(200, 0))
        util.waitTouch(images.getm("liudao,shishenlu"), offset=(0, 225))
        util.waitTouch(images.getm("liudao,shishenlu"), offset=(0, 225))
        hasConfirmBtn()
        changeTeam()
        sortTouch(images.getm("liudao,btn_confirm_b"))
        sleep(1)
    return True


def chooseEvent():
    global attackNum
    list = [
        "guanka_shenmi",
        "guanka_ningxi",
        "guanka_hundun",
        "guanka_xingzhiyu",
        "guanka_aozhan",
        "guanka_boss",
    ]
    _value = None
    for item in list:
        _item = find_all(images.getm("liudao," + item))
        if _item:
            if item != "guanka_boss":
                util.moveTouch(images.getm("liudao," + item))
            _value = eventActionRun(item)
            if _value:
                if item == "guanka_boss":
                    util.log("Liudao", "2")
                    return True
                attackNum += 1
                util.log("Liudao", "1")
            break
    if _value == None:
        return False
    return chooseEvent()


def eventActionRun(_key):
    global buffNum
    util.sleep(1)
    if _key == "":
        return False
    elif _key == "guanka_shenmi":
        fangzao = find_all(images.getm("liudao,btn_fangzao"))
        if fangzao and buffNum < 4:
            util.findTouch(images.getm("liudao,icon_buff_small"))
            util.sleep(1)
            util.touch(fangzao)
            confirmBack = util.waitTouch(getImage("pop_btn_confirm2"), timeout=4)
            if confirmBack:
                buffNum += 1
            util.sleep(0.5)
        util.waitTouch(images.getm("liudao,back"))
    elif _key == "guanka_ningxi":
        util.sleep(2)
        buff = find_all(images.getm("liudao,icon_buff_small"))
        if buff:
            util.touch(buff, offset=(0, 160))
            util.sleep(0.5)
            confirmBn = find_all(getImage("pop_btn_confirm2"))
            if confirmBn:
                util.touch(confirmBn)
                buffNum += 1
                util.sleep(0.5)
        util.waitTouch(images.getm("liudao,btn_move"))
    elif _key == "guanka_hundun":
        jingying = find_all(images.getm("liudao,attack_jingying"))
        movebtn = find_all(images.getm("liudao,btn_move"))
        if jingying:
            util.sleep(1)
            util.findTouch(images.getm("liudao,attack_jingying"), offset=(100, 120))
            util.waitTouch(images.getm("liudao,entry_attack_in"))
            util.sleep(5)
            util.wait(images.getm("liudao,beizhan"), timeout=120)
            chooseBuff()
            chooseBuff()
            util.waitTouch(images.getm("liudao,success_gift"), touchtime=1)
        elif movebtn:
            util.touch(movebtn)
    elif _key == "guanka_xingzhiyu":
        util.waitTouch(images.getm("liudao,attack_iden"), offset=(100, 120))
        util.waitTouch(images.getm("liudao,entry_attack_in"))
        util.waitTouch(images.getm("liudao,success_gift"), timeout=120)
    elif _key == "guanka_aozhan":
        sortTouch(images.getm("liudao,attack_iden"), index=-1, touchtime=1)
        util.waitTouch(images.getm("liudao,entry_attack_in"))
        sleep(5)
        util.wait(images.getm("liudao,beizhan"), timeout=120)
        chooseBuff()
        util.waitTouch(images.getm("liudao,success_gift"), touchtime=0.5)
    elif _key == "guanka_boss":
        changeTeam(True)
        util.waitTouch(images.getm("liudao,entry_attack_in"))
        util.sleep(20)
        util.waitTouch(
            images.getm("liudao,boss_gift"), timeout=220, offset=(-200, 0), touchtime=1
        )
        util.sleep(0.5)
        util.touch((100, 300))
    if _key != "guanka_boss":
        beizhanIden = util.wait(images.getm("liudao,beizhan"), timeout=4)
        if not beizhanIden:
            util.touch((100, 300))
    util.sleep(1)
    return True


def chooseBuff(refresh=False):
    global attackNum
    global buffNum
    index = -1
    buff = find_all(images.getm("liudao,icon_buff"))
    if buffNum < 4 and attackNum > 8:
        maxNum = 3
        while not buff and maxNum > 0:
            maxNum -= 1
            util.waitTouch(images.getm("liudao,btn_refresh"))
            util.sleep(1)
            buff = find_all(images.getm("liudao,icon_buff"))
    if buff:
        buffNum += 1
        sortTouch(
            images.getm("liudao,btn_confirm_b"), index=0, value=buff[0]["result"][0]
        )
    else:
        sortTouch(images.getm("liudao,btn_confirm_b"), index)
    sleep(1)


def changeTeam(isBoss=False):
    global firstAction
    util.waitTouch(images.getm("liudao,beizhan"))
    util.waitTouch(images.getm("liudao,shishenlu"))
    if firstAction:
        util.changeTeams("liudao_base")
        util.waitTouch(images.getm("liudao,shishenlu"))
        firstAction = False
    util.changeTeams("liudao_boss" if isBoss else "liudao_normal", temp=True)
    util.waitTouch(images.getm("team_back"))
    util.sleep(1)


def hasConfirmBtn():
    util.sleep(0.5)
    confirmbtn = find_all(
        Template(
            images.get("fight_back_confirm"),
            record_pos=(0.091, 0.056),
            resolution=(2208, 1242),
        )
    )
    if confirmbtn:
        util.touch(confirmbtn)


def sortTouch(img, index=0, loc=0, value=0, touchtime=0):
    target = util.wait(img, more=True, touchtime=touchtime)
    if not target:
        return False
    target = sorted(target, key=lambda x: abs(x["result"][loc] - value))
    return util.touch(target[index])


def fixScene():
    print("fixScene")
    key = find_all(images.getm("liudao,btn_move"))
    if key:
        util.findTouch(images.getm("liudao,btn_cancel"))
        util.touch(key)
        util.sleep(1)
        return
    key = find_all(images.getm("liudao,attack_jingying"))
    if key:
        return eventActionRun("guanka_hundun")
    key = find_all(images.getm("liudao,attack_iden"))
    if key:
        return eventActionRun("guanka_aozhan")
    key = find_all(images.getm("liudao,guanka_boss"))
    if key:
        return eventActionRun("guanka_boss")
    key = find_all(images.getm("liudao,back"))
    if key: ## 神秘标识
        return eventActionRun("guanka_shenmi")
    return util.touch((100, 300))
