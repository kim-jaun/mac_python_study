l1 = list(range(5)) # 0 5까지 숫자 생성
print(l1)
del l1[::2] # 처음부터 짝수번쨰 데이터 삭데
print(l1)
l1.append(5)
print(l1)
l1[0:0] = [67]
print(l1)