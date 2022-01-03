x = [2, 3, 5, 7, 11]
y = x  # x의 주소를 y에 대입
# call by value, call by reference 함수 부를 때 매개변수
y[2] = 4
# y를 변경했더니 x도 같이 변경경print(x)
print(y)

