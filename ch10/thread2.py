import time, threading
def ThredEx(id):
    for i in range(10):
        print(f'id={id} --> {i}')
        time.sleep(1) # 1초 대기
for i in range(2):
    id = (f"{i}번 쓰레드")
    th = threading.Thread(target=ThredEx, args=(id,))
    th.start()