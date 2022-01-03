print("문자를 입력하세요")
a = input()
print(a)
print(a[::-1])
l = len(a)
while l > 0:
    l -= 1
    print(a[l], end="")
# 길이 - 1: 마지막 인덱스
#           마지막부터 -1보다 클때까지(즉 인덱스 0) 1씩빼기
print("\n=========")
l = len(a)
for i in range(l-1,-1,-1):
    print(a[i], end="")
