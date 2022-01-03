from abc import *
class Employ(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
    @abstractclassmethod
    def cal_sla(self):
        pass
    def bonus(self):
        self.sal = self.cal_sla()
        self.bonus = self.sal * 0.1
    def prn(self):
        print("======================")
        print(f"이름 : {self.name}")
        print(f"급여 : {self.sal:.2f}")
        print(f"보너스 : {self.bonus:.2f}")

class SalaryMan(Employ):
    def __init__(self, name, annual):
        super().__init__(name)
        self.annual = annual
    def cal_sla(self):
        return self.annual / 12
    def prn(self):
        super(SalaryMan, self).prn()
        print(f"연봉 : {self.annual}")

class HourlyMan(Employ):
    def __init__(self, name, work_hour, money_per_hour):
        super().__init__(name)
        self.work_hour = work_hour;
        self.money_per_hour = money_per_hour;
    def cal_sla(self):
        return self.work_hour * self.money_per_hour
    def prn(self):
        super(HourlyMan, self).prn()
        print(f"단가 : {self.money_per_hour}원")
        print(f"근무 : {self.work_hour}시간")

s1 = SalaryMan("보검", 50000000)
s2 = SalaryMan("로제", 70000000)
h1 = HourlyMan("아이유", 20, 18000)
h2 = HourlyMan("차은우", 50, 7000)

emps = [s1, s2, h1, h2]
for emp in emps:
    emp.bonus()
    emp.prn()