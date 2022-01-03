class Person:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
    def prn(self):
        print("====================")
        print(f"이름 : {self.name}")
        print(f"나이 : {self.age}")

class Student(Person):
    def __init__(self,name, age, hobby):
        super().__init__(name, age)
        self.hobby = hobby;
    def prn(self):
        super().prn()
        print(f"취미 : {self.hobby}")

class Teacher(Person):
    def __init__(self,name, age, major):
        super().__init__(name, age)
        self.major = major;
    def prn(self):
        super().prn()
        print(f"과목 : {self.major}")

class Manager(Person):
    def __init__(self,name, age, part):
        super().__init__(name, age)
        self.part = part;
    def prn(self):
        super().prn()
        print(f"담당 : {self.part}")

st1 = Student("보검", 27, "졸기")
st2 = Student("리사", 25, "울기")
th1 = Teacher("재석", 50, "자바")
th2 = Teacher("로제", 28, "python")
mg1 = Manager("명수", 51, "화장실 청소")
mg2 = Manager("차은우", 31, "운전")
x = [st1, st2, th1, th2, mg1, mg2]
for s in x:
    s.prn()