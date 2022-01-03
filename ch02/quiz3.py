#        2    +    3 => 5     >     12   +> f
print(int(2.5) + int(3.8) > int(str(1) + str(2)))
#       t       and not f=> t => t  or  f => t
print((12 >= 10 and not 3 > 4) or 3 ** 2 != 9)
#      t   and      t => t
print(True and (True or False))
#       f      or      f => f
print(not True or (True and False))
#     t
print(False == False)