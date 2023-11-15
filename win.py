import win32gui


def getAllWin():
    wins = []
    win32gui.EnumWindows(lambda h, param: param.append(h), wins)
    wins = [(i, getWinName(i)) for i in wins]
    return wins


def getWinName(id):
    return win32gui.GetWindowText(id)


def findWinIdByText(t, list):
    targets = []
    for i in list:
        if t in i[1]:
            targets.append(i)
    return targets

print(findWinIdByText("MuMuPlayer",getAllWin()))
