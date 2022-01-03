print("월을 입력하세요")
month = int(input())
# in은 포함여부 반대는 not in
if month in [1,3,5,6,10,12]:
    day = 31
else :
     day = 28 if month==2 else 30;
print(f"{month}는 마지막 날자가 {day}입니다")