# 4! = 4 * 3 * 2 * 1, 6! = 6 * 5 * 4 * 3 * 2 * 1
def fat1(num):
    if num > 1:
        return fat1(num - 1) * num # f(3)*4= f(2)*3*4=>f(1) *2 * 3 * 4=>1*2*3*4
    else:
        return 1
print(fat1(4))
print(fat1(6))