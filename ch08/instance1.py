from abc import *
class Car(metaclass=ABCMeta):
    @abstractclassmethod
    def drive(self):
        pass
class Ambulance(Car):
    def drive(self):
        print("환자를 싣고 달린다")
    def move(self):
        print("경적을 울리면서 달린다")

class Taxi(Car):
    def drive(self):
        print("총알처럼 달린다")

cars = [Ambulance(), Taxi()]
for car in cars:
    car.drive()
    if isinstance(car, Ambulance): # 현재 car가 Ambulance에서 생성된 객체
        car.move()