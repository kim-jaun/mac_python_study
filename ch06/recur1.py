# 자신의 함수를 호출 : 재귀함수(recurxive function)
def f1(cnt):
    if (cnt > 0):
        print('현재 :', cnt)
        f1(cnt - 1) # 매개변수의 변경이 없으면 무한 루프
    print('결과 :',cnt)

f1(5)