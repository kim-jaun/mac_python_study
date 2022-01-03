def fat1(num):
    result = 1
    for i in range(num,1, -1):
        print(i,'* ',end='')
        result *= i
    print('1 =',end='')
    return result

print(fat1(4))
print(fat1(6))