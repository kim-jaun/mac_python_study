import random
cnt = 0;
# 1과 100사이 랜덤한 정수 발생
ran = random.randint(1, 100)
while True:
    print("1 ~ 100사이 숫자를 입력하세요")
    num = int(input())
    cnt += 1
    if num == ran:      break;
    elif num > ran:     print("작은 수를 입력하세요")
    else:       print("큰수를 입력하세요")
print(f"{cnt}에 정답 {ran}을 맞췄습니다")
