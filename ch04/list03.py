a = [1,2,3]
a[1] = 15   # 문자열은 특정 위치값을 변경할 수 없지만 list는 가능
print(a)
del a[1]    # 특정 인덱스 데이터 삭제
print(a)
a2 = [1,2,3,4,5]
del a2[2:]
print(a2)
a3 = [3,6,2, 4]
a3.append(7) # list에 데이터 뒤에 추가
print(a3)
a3.sort()  # 정열
print(a3)
a4 = ['a','t','d','b']
a4.sort()  # 정열
print(a4)
a5 = ['a','t','d','b']
a5.reverse()  # 순서를 반대로
print(a5)