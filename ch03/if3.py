print("남자/여자 중에서 입력하시오")
gender = input()
print("팔굽혀 펴기 갯수를 입력하시오")
cnt = int(input())
if gender=="남자":
    if cnt >= 10:
        print("합격")
    else:
        print("불합격")
else:
    if cnt >= 5:
        print("합격")
    else:
        print("불합격")