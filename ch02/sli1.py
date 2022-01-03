#     0123456789012345678901234567890123
a1 = "Life is too short, You need Python"
# 인덱스에 해당하는 문자 가져오기, -1은 맨 뒤
print(a1[0], a1[3], a1[-1], a1[-2])
print(a1[0:4], a1[:4]) # 인덱스 0부터 4앞(인덱스 3)까지 문자, 처음부터 인덱스 4앞까지
print(a1[4:],':', a1[23:27]) # 인덱스 4부터 끝까지 java의 substring과 유사
print(a1[:])
print(a1[19:-5])

#    0123456789012
a = "20010331Rainy"
weather = a[8:]
year = a[:4]
date = a[4:8]
print(weather)
print(year)
print(date)
