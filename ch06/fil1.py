# def positive(x):
#    return x > 0
positive = lambda x: x>0
l1 = [1, 3, -2,0,-5,6]
print(list(filter(positive, l1)))