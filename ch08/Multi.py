class Person:
    def speak(self):
        print("떠든다")
    def move(self):
        print("두발로 걷는다")

class Fish:
    def move(self):
        print("지느러미를 사용하여 헤엄친다")

class MurMaid(Fish, Person): # 다중상속에서 중복된 메서드는 먼저 상속되는 것으로 사용한다
    pass

mm = MurMaid()
mm.speak()
mm.move()