import utils.base.file as file


filePath = "config/index.json"
fileSwitchPath = "config/switch.json"
fileInfo = None
fileSwitch = None


def initInfo():
    global filePath
    global fileSwitchPath
    global fileInfo
    global fileSwitch
    file.fileWatcher(fileSwitchPath, backevent=infoFileChange)
    fileInfo = file.readJSONFile(filePath)
    fileSwitch = file.readJSONFile(fileSwitchPath)


def infoFileChange(e: file.FileModifiedEvent):
    global fileSwitch
    global fileSwitchPath
    if e.event_type == "modified":
        fileSwitch = file.readJSONFile(fileSwitchPath)


def getInfo(k="m"):
    global fileInfo
    global fileSwitch
    if not fileInfo:
        initInfo()
    if k == "s":
        return fileSwitch
    return fileInfo


def setInfo(data):
    global fileInfo
    for item in data:
        value = data[item]
        setJSONData(json=fileInfo, key=item, value=value)
    file.editJSONFile(filePath, fileInfo)


def setJSONData(json, key: str, value):
    keys = key.split(".")
    if len(keys) > 1:
        target = None
        # $d+ change number
        for _i, _k in enumerate(keys):
            if "$" in _k:
                keys[_i] = int(_k.replace("$", ""))
        for _i in range(len(keys) - 1):
            target = json[keys[_i]]
        target[keys[len(keys) - 1]] = value
    else:
        json[key] = value


def close():
    file.closeFileWatcher()