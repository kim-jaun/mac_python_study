file = open('chicken.txt','r',encoding='utf-8')
for line in file: # 데이터 한줄씩  line에 전달
    print(line, end="")
file.close()    # 종료하면 다썼다고 표시