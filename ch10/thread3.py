import time, threading
class ThreadEx(threading.Thread):
    def run(self) -> None:
        for i in range(10):
            print(f'id={i} --> {self.getName()}')
            time.sleep(1)
for i in range(2):
    th = ThreadEx()
    th.start()