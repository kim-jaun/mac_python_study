# 675 = 6+7+5=>18, 234=2+3+4 => 9
print("숫자를 입력하세요")
num = int(input())
sum = 0
s_num = str(num)
for i in range(len(s_num)):
    sum += int(s_num[i]) # 6 7 5
print("자리수 합 :",sum)