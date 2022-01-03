# 빈 리스트 만들기
numbers = []
# numbers에 자연수 1부터 10까지 추가
numbers[0:0] = range(1, 11)
print(numbers)
# numbers에서 홀수 제거
del numbers[::2]  # 인덱스 짝수번째 데이터 삭제
# del numbers[1::2]  # 인덱스 홀수번째 데이터 삭제
print(numbers)
# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers[0] = 20
print(numbers)
# numbers를 정렬해서 출력
numbers.sort()
print(numbers)