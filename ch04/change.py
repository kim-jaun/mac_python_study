# 거스름돈 구하기
print("지불한 돈")
payment = int(input())
print("구매한 물건 값")
cost = int(input())
money = payment - cost # 거스름 받을 돈
unit = [50000, 10000, 5000, 1000]
for i in unit:
    print(f"{i}짜리 지폐 : {money//i}")
    money %= i