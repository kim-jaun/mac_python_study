def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(10))
print(fibo(2))
# 1, 1, 2, 3, 5
print(fibo(5))