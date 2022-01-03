sum = 0
i = 1
while i <=1000:
    if i % 3 == 0:
        sum += i
    i += 1
print(f"3의 배수 합계 : {sum}")