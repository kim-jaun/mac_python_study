class Student:
    @classmethod
    def cmethod(cls):
        print("클래스 메서드")
        print(cls)
    @staticmethod
    def smethod():
        print("정적 메서드")

Student.cmethod()
Student.smethod()