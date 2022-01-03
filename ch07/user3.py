class User:
    def initialize(self, name, age, tel):
        self.name = name; self.age = age; self.tel = tel;
    def indroduce(user):
        print(f"이름 : {user.name}, 나이 : {user.age}, 전화 : {user.tel}")

user1 = User(); user1.initialize("로사",25,"010-1111-1234")
user2 = User(); user2.initialize("보검",29,"010-2222-1234")
User.indroduce(user1); User.indroduce(user2)
user1.indroduce(); user2.indroduce()
