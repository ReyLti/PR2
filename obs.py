from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("on_created", event.src_path)
        
    def on_modified(self, event):
        print("on_modified", event.src_path)
        g = "aeiou"
        file = open(event.src_path)
        for k in file.read():
            if k in g: print(str(k).lower())
            else: print(str(k).upper())



event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path=r"C:\Users\ReyLpol\Desktop\PR2", recursive=False)
observer.start()
while True:
    try:
        pass
    except KeyboardInterrupt:
        observer.stop()
