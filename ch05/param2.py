# **변수 키=값
def f(weight, height, **k):
    print(weight, height)
    print(k)

f(weight=67, height=170, age=25, color="빨강")