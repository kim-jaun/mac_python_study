str = "c:\\data\\data.txt"
# test라는 문자가 있는가 ?
print(str.find('test'))
# 확장자만 출력
n = str.rfind(".") # .이 있는 인덱스 번호
print(str[(n+1):]) # 그 인덱스 번호 다음부터 끝까지
list = str.split(".") # .을 기준으로 리스트로 변환
print(list)
print('확장자 :',list[len(list) - 1])