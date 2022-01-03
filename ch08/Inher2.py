class Base:
    def __init__(self, name):
        print("Base __init__")
        self.message = "안녕"
        print(name)

class Child(Base):
    def __init__(self):
        super().__init__("로사")
        print("Child __init__")
    def prt(self):
        print(self.message) # 부모의 생성자 호출, 위치는 다 된다

ch = Child() #Child의 __init__ 실행하지만 부모는 반드시 호출해야 __init__가 실행
ch.prt()