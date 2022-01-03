# *변수 : 값만 보낼 때
def f(weight, height, *k):
    print(weight, height)
    print(k)

f(67, 170, 25, "빨강")