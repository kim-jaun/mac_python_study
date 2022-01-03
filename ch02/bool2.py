x = 3
#      f     or     f    or   f = f => false
print(x > 4 or (x < 2 or x != 3))
#       f     and     t =>f or    t => t
print((4 < 3 and 12 > 10) or 7 == 7)
print(not 4 < 3)
print(not not True)