a = [1,2,3]
print(a.index(3)) # 글자 3인 있는 인덱스
print(a.index(1))
# print(a.index(0)) # 없는 데이터의 인덱스를 물어보면 에러 발생
a2 = [2, 6, 7]
a2.append(12)
print(a2)
a2.insert(1, 23) # 인덱스 1에 23추가 나머지는 뒤로 밀림
print(a2)
a2.remove(7)  # 값 7삭제, del(인덱스), remove(값)
print(a2)

# FIFO queue
a3 = [1,2,3]
print(a3.pop())  # 맨 마지막 글자를 추출하여 사용하고 버람
print(a3)

a4 = [3,7,5]
print(a4.pop(1))  # 인덱스 1번쨰 글자를 추출하여 사용하고 버람
print(a4)