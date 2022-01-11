import time, threading
class Th1(threading.Thread):
    def run(self) -> None:
        i = 0
        while True:
            i += 1
            print(f'i = {i}')
            time.sleep(0.1)
            if i > 100: break
th = Th1()
# main이 끝나면 주변의 thread도 종료 시킨다.
# start1ㅗ다 앞에 있어야 한다
th.daemon = True
th.start()
for j in range(10):
    time.sleep(0.1)
    print(f"j = {j}")