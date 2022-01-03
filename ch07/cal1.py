def plus(x, y):
    return x + y
def minus(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

# 실행하는 모듈의 이름이 자기 모듈이면 실행
if __name__ == "__main__":
    print(multiply(12,3))
    print(divide(10, 4))