file = open('chicken.txt','r',encoding='utf-8')
sum = 0
for line in file: # 데이터 한줄씩  line에 전달
    # strip()는 공백 \n등을 삭제
    data = line.strip().split(": ")
    sum += int(data[1])
    print(f"{data[0]}일 : {data[1]}")
print("===============")
print(f"총매출 : {sum}")
file.close()    # 종료하면 다썼다고 표시