def hello_kor():
    print("안녕하세요")
def hello_eng():
    print("Hello !!")
def greet(h):
    h()

# 매개변수에 함수명을 전달 가능
greet(hello_kor)
greet(hello_eng)