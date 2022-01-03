def f1(num):
    print('num =',num)
p = f1 # 함수를 변수처럼 전달가능
p(10)
p("대박")

def plus(x, y):
    print(x + y)
def minus(x,y):
    print(x  -y)

p2 = [plus, minus]
p2[0](10,20)
p2[1](10,20)