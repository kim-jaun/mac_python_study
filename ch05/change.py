def cal_change(payment, cost):
    money = payment - cost
    unit = [50000, 10000, 5000, 1000]
    for i in unit:
        print(f"{i}원짜리 지폐 : {money//i}장")
        money %= i;
cal_change(100000, 33000)
print("=================")
cal_change(500000, 378000)