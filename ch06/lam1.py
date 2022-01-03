def f(x):
    return x * x
li = [1,2,3,4,5]
# 함수와 반복문으로 처리
for i in li:
    print(f(i), end=' ')
# map을 사용
print("\n==============")
# map은 list의 각각의 값에 함수 적용
print(list(map(f, li)))
# lamda을 사용
print("==============")
# 각각의 list값을 lambda식을 반영하여 처리
print(list(map(lambda x:x*x,li)))
# filter 조건이 true데이터 만 추출
print(list(filter(lambda x:x%2==1,li)))