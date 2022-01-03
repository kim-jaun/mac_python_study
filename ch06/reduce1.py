from functools import reduce
a = [47, 11, 42, 13, 103]
print(reduce(lambda x, y: x+y, a))
print(reduce(lambda x, y: x-y, a))
# k = x if x>y else y 두수를 비교해서 x가 크면 k는 x 아니면 k는 y
print(reduce(lambda x, y: x if x>y else y, a))