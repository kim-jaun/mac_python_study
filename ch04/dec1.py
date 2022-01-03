from decimal import *
sum = Decimal(0.0) # 실수 0.0인데 정확한 수
delta = Decimal('0.1') # 실수 정확한 0.1
for i in range(1000):
    sum += delta
print(f"합계 : {sum}")

sum1 = 0.0;
for j in range(1000):
    sum1 += 0.1
print(f"합계 : {sum1}")