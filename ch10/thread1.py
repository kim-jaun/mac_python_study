import  time
def ThredEx(id):
    for i in range(10):
        print(f'id={id} --> {i}')
        time.sleep(1) # 1초 대기
for i in range(2):
    ThredEx(f"{i}번 쓰레드")