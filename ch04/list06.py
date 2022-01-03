n1 = [1,2,3,4,5]
result = []
# 홓수 데이터만 제곱하여 resut에 저장
for n in n1:
    if n % 2 == 1:
        result.append(n**2)
print(result)