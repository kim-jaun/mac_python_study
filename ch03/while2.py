num = int(input("구구단 숫자 : "))
print(f"구구단 {num}단")
i = 0
while i < 9:
    i += 1;
    print(f"{num} * {i} = {num*i}")
else: # true가 아니면
    print("프로그램 종료")