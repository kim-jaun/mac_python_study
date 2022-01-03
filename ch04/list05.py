a1 = [1,7,6,5,1,3,1,2]
print(a1.count(1))  # 1의 갯수
a1.extend([11,12])  # 11,12를 가진 list추가, +와 유사
print(a1)
#         0       1     2       3
names = ["윤수", "혜린", "태호", "영훈"]
#          -4    -3      -2     -1
print(names[2], names[-2])
names[1] = "로사"
print(names)