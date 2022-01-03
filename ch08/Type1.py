class StaticClass:
    attr = "정적 클래스"

ob1 = StaticClass()
print(ob1.attr)
# type을 사용하여 동적으로 객체 생성
ob2 = type("DynamicClass", (), {'attr':'복많이 받으세요'})
print(ob2.attr)