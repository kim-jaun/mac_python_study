class User:
    # __init__메서드는 자바의 생성자 역할
    def __init__(self, name, age, tel):
        self.name = name; self.age = age; self.tel = tel;
    def indroduce(user):
        print(f"이름 : {user.name}, 나이 : {user.age}, 전화 : {user.tel}")

user1 = User("로사",25,"010-1111-1234")
user2 = User("보검",29,"010-2222-1234")
User.indroduce(user1); User.indroduce(user2)
user1.indroduce(); user2.indroduce()
