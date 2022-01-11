import os
import shutil
# ./ 현재 디렉토리 ../ 상위 디렉토리
curlist = os.listdir("./")
# curlist = os.listdir("./ch08")
for i in curlist:
    print(i)
print("현재 디렉토리 정보")
print(os.stat("./"))
# 디렉 생성
# os.mkdir("temp")
# os.rmdir("temp")  # 디렉토리가 비어있을때 삭제
shutil.rmtree("temp")   # 디렉토리가 비어있지 않아도 삭제