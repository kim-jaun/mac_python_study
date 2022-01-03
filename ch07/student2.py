class Student:
    school_name = "한국" # 클래스 변수, 객체를 생성하지 않고 사용 가능하다
    def setName(self, name):
        self.name = name;
    def getName(self):
        return self.name
    def setAge(self, age):
        if age < 0:
            self.age = 0
            print("나이는 0보다 커야 합니다")
        else:
            self.age = age
    def getAge(self):
        return self.age
st1 = Student(); st2 = Student();
# st2.age = -10
st1.setName("철수"); st1.setAge(52)
st2.setName("보검"); st2.setAge(-27)
print(f"st1의 이름 : {st1.getName()}")
print(f"st2의 나이 : {st2.getAge()}")
print(f"{Student.school_name}")
