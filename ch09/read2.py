file = open('test.txt','r', encoding='utf-8')
content = file.read() # 한꺼번에 데이터 읽기
print(content)
file.close()
print("===========")
file = open('test.txt','r', encoding='utf-8')
for line in file: # 데이터 한줄씩 처리
    print(line, end="")
file.close()
file = open('test.txt','r', encoding='utf-8')
lines = file.readlines() # list형식으로 데이터 일기
print(lines)
file.close()