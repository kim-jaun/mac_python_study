class Callable:
    def __call__(self, *args, **kwds):
        print("나 불렀어")

ob = Callable();
ob() # 객체를 메서드처럼 호출하면 __call__ 메서드가 실행