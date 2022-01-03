class A:
    def m1(self):
        print("M1")
    def m2(self):
        print("M2")
class A1(A):
    def m2(self):
        print("A1의 M2")
class A2(A):
    def m1(self):
        print("A2의 M1")

a1 = A1(); a1.m1(); a1.m2();
a2 = A2(); a2.m1(); a2.m2();