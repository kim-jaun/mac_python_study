a = [1, 2, 3, 4, 5]
print(a[:2])
print(a[2:])
#     0  1  2    3             4  5
a2 = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a2[2:])
print(a2[3][1:])

b1 = [1,2,3]
b2 = [3,4,5]
print(b1 + b2)
print(b1 * 3)
print(len(b1))
print(str(b1[1])+"hi")