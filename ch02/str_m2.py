k1 = "abd1234"
print(k1.isalpha())   # 알파벳으로만 구성됐는지 여부
print(k1.isnumeric()) # 숫자로만      "
print(k1.isalnum())   # 알파벳과 숫자로   "

k2 = "Hello World"
print(k2.replace("World","Korea")) # 데이터 변경

k3 = "대박, 사건, 추어, 이리와"
k4 = k3.split(",") # 컴마를 기준으로 list형식으로 변경
print(k4)

k5 = "How Are you ?"
print(k5.upper()) # 대문자로 변경
print(k5.lower()) # 소문자로 변경
print("내 이름은 {}입니다. 나이는 {}살이다".format("로제",25))
print("내 이름은 {0}입니다. 나이는 {1}살이다".format("로제",25))
print("내 이름은 {1}입니다. 나이는 {0}살이다".format("로제",25))

print(", ".join("abcd")) # 문자와 문자 사이에 들어갈 문자를 정의