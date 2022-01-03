from abc import *
class A1 (metaclass=ABCMeta):
    def prn(self):
        print("새해에 대박 나세요")
    @abstractclassmethod
    def disp(self): # 추상메서드
        pass

class A2(A1):
    def m1(self):
        print("복많이 받으세요")
    def disp(self): # 추상 클래스를 상속 받으면 반드시 재정의 해야한다
        print("재정의 했습니다")

a2 = A2()
a2.prn(); a2.disp(); a2.m1()