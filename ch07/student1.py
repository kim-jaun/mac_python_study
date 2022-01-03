class Student:
    def start(self):
        print("안녕! 컴 동지들")
    def print_name(self, name):
        print(f"내이름은 {name}이야")

st1 = Student();
st1.start()
Student.print_name(st1,"로제")
Student.start(st1)
st1.print_name("보검")