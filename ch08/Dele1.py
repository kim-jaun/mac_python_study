class Delegation:
    def __init__(self, st):
        self.st = st
    def __getattr__(self, item): # 없는 메서드를 요청하면 __getattr__가 대신 실행
        print(f"위임 {item}", end=" ")
        return getattr(self.st, item)

st = "Good Morning My Friend"
d1 = Delegation(st)
print(d1.count('n'))
print(d1.find("d"))
print(d1.rfind("d"))