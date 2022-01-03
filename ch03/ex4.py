print("수박의 무게를 입력하세요")
weight = int(input())
if weight > 10:
    print("1등급")
elif weight > 7:
    print("2등급")
elif weight > 4:
    print("3등급")
else:
    print("4등급")