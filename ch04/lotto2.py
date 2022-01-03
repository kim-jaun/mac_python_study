from random import randint
numbers = set()
while len(numbers) < 6:
    ran = randint(1, 45) # 정수 1 ~ 45(1rhk 45포함)사이에 램덤한 숫자
    numbers.add(ran)
print(sorted(numbers))