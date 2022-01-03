grades = [[62,75,77],[78,81,86],[85,91,89]] # 중첩리스트
print(grades[0])
print(grades[1][1])
a1 = [1, 7, 6, 5, 3]
# a1.sort() # a1이 sort돤 상태로 변경, 오름차순 정열
a2 = sorted(a1) # a1은 그대로이고 a2는 정열된 결과가 저장
print(a2)
print(a1)
a1.reverse() # 순서를 반대로
print(a1)
a1.sort(reverse=True) # 데이터 내림차순 정열
print(a1)
a2 = sorted(a1, reverse=True) # a1은 변화가 없고 내림차순으로 된 결과가 a2에 저장
print(a2)