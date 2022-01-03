class MyDeco:
    def __init__(self, func):
        print("데코레이트 초기화")
        self.func = func
    def __call__(self, *args, **kwds):
        print(f"시작 {self.func.__name__}")
        self.func()
        print(f"종료 {self.func.__name__}")
@MyDeco
def print_hello(): # 클래스와 관계없는 메서드
    print("안녕")

print_hello()