class Student:
    def __init__(self, name="무명"):
        self.__name = name;     # __변수 : name의 멤버변수는 private이라는 의미
    def setName(self, name):
        print("setter method사용")
        self.__name = name;
    def getName(self):
        print("getter method사용")
        return self.__name
    def setAge(self, age):
        print("setter method사용")
        if age < 0:
            print('나이는 0보다 작을 수 없습니다')
            self.__age = 0
        else :
            self.__age = age;
    def getAge(self):
        print("getter method사용")
        return self.__age
    name = property(fset=setName, fget=getName)
    age = property(getAge, setAge) # setter method가 멎저오고, getter method뒤에 있을 때는 fset,fget 생략 가능

st1 = Student()
st1.name = "보검" # 변수에 직접 저장해도 메서드를 사용한다
st1.age = -4
print(st1.name, st1.age)