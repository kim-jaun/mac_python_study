from time import ctime
class Student:
    def __init__(self, name="무명씨"): # 객체가 생성될 때 실행
        print(f"{ctime()}에 객체가 생성되었습니다")
        self.name = name
    school_name = "한국"
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def __del__(self):  # 객체가 삭제될 때 실행
        print(f"{ctime()}에 객체가 소멸 되었습니다")
st1 = Student("로사"); st2 = Student()
print(f"st1의 이름 {st1.getName()}")
print(f"st2의 이름 {st2.getName()}")
# del st1
# del st2