def f1():
    x  = 7
x = 1
f1()
print("f1 :",x)
def f2():
    global y # 함수안과 함수 밖을 같이 사용
    y  = 7
y = 1
f2()
print("f2 :",y)