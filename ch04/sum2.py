# 675 = 6+7+5=>18, 234=2+3+4 => 9
# 문자로 바꾸지 말고 자리수 합계를 구하시오
print("숫자를 입력하세요")
num = int(input())
sum = 0
while num != 0:
    sum += num % 10    # 5  7  6
    num =  num // 10   # 67 6  0
print("자리수 합 :",sum)