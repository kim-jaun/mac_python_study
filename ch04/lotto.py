from random import randint
numbers = []
while len(numbers) < 6:
    ran = randint(1, 45) # 정수 1 ~ 45(1rhk 45포함)사이에 램덤한 숫자
    if ran not in numbers: # 자바에서 for문사용하여 같은 값이 있는지 검사
        numbers.append(ran)
print(sorted(numbers))