class Base:
    def m1(self):
        print("부모 메서드")

class Child(Base): # python 부모의 클래스명을 괄호에 넣는다
    def m2(self):
        print("자식 메서드")

b1 = Base(); b1.m1(); # b1.m2()
c1 = Child(); c1.m1(); c1.m2(); # 부모의 멤버변수나 메서드를 자기것으로 이용