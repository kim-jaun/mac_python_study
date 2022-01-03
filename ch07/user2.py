class User:
    def indroduce(user):
        print(f"이름 : {user.name}, 나이 : {user.age}, 전화 : {user.tel}")

user1 = User(); user1.name = "로사"; user1.age = 25; user1.tel = "010-1111-1234"
user2 = User(); user2.name = "보검"; user2.age = 29; user2.tel = "010-2222-1234"
User.indroduce(user1); User.indroduce(user2)
user1.indroduce(); user2.indroduce()
