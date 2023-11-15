from airtest.core.api import *
import utils.index as util
import re
import threading

closeThread = False
threader = None
modelName = "Watcher"


def main():
    threadOpen(watchData)


def threadOpen(target, args=()):
    global threader
    th = threader = threading.Thread(target=target, args=args)
    th.start()


def watchData():
    global modelName
    global closeThread
    util.print_(modelName, "Open watcher~")
    index = 0
    atype = 0
    while not closeThread:
        util.sleep(10)
        index += 1
        back = watchAction(index, atype)
        if back > 0:
            index = back
            atype += 1
        elif back == -1:
            atype = 0
            index = 0

laststr = None
def watchAction(t=0, a=0):
    global laststr
    global modelName
    t1 = 12
    t2 = 12
    t3 = 24
    if t % t1 == 0 and a == 0:
        if laststr == None:
            laststr = "".join(re.findall("\d+", util.getLog()))
            return 0
        strdata = "".join(re.findall("\d+", util.getLog()))
        if laststr == strdata:
            util.print_(modelName, "First fix scene", laststr, strdata)
            util.expeditedRepair()
            return 1
        else:
            laststr = strdata
            util.print_(modelName, ".")
    elif a == 1 and t > t2:
        strdata = "".join(re.findall("\d+", util.getLog()))
        if laststr == strdata:
            timeindex = 10
            while timeindex > 0:
                headvalue = "About to restart the app, " if timeindex == 10 else ""
                util.print_(modelName, f"{headvalue} Count down {timeindex}s <")
                timeindex -= 1
                sleep(1)
            util.print_(modelName, "Restart the game")
            return 1
        else:
            laststr = strdata
            return -1
    elif a == 2 and t > t3:
        util.print_(modelName, "Fix end.")
        laststr = None
        return -1
    return 0


def close():
    global closeThread
    closeThread = True
