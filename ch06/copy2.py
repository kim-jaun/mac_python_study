import copy
a1 = [1,2,3]
#    0    1
x = [a1, 100]           # x는 a1주소의 값을 가져오고 값 100
y1 = copy.copy(x)       # y1은 a1주소값과 100이라는 값을 저장
y2 = copy.deepcopy(x)   # y2는 a1주소에 있는 값을 읽어서 가져오고 100이라는 값을 가져온다
x[1] = 200
print(y1, y2)
a1[1] = 15
print(y1, y2)