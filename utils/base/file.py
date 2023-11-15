import json
import time
import threading


def readJSONFile(path):
    file_data = open(path, "r", encoding="utf-8")
    data = file_data.read()
    datajson = json.loads(data)
    file_data.close()
    return datajson


def editJSONFile(path, data):
    file_write = open(path, "w", encoding="utf-8")
    file_write.write(json.dumps(data, indent=2, ensure_ascii=False))
    file_write.close()
    return data


# watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileModifiedEvent


class MyHandler(FileSystemEventHandler):
    def __init__(self, backevent) -> None:
        self.backevent = backevent
        super().__init__()

    def on_modified(self, event: FileModifiedEvent):
        self.backevent(event)

    def on_created(self, event: FileModifiedEvent):
        self.backevent(event)


def fileWatcher(path, backevent):
    fileWatcherThread = threading.Thread(
        target=fileWatcherInner, args=(path, backevent)
    )
    fileWatcherThread.start()
    return fileWatcherThread

closeWatcher = False
observerWatcher = None
def fileWatcherInner(path, backevent):
    global closeWatcher
    global observerWatcher
    event_handler = MyHandler(backevent)
    observer = Observer()
    observerWatcher = observer
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while not closeWatcher:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def closeFileWatcher():
    global closeWatcher
    global observerWatcher
    closeWatcher = True
    observerWatcher.stop()
