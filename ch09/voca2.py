in_file = open('voca.txt','r', encoding='utf-8')
for line in in_file:
    # 데이터 한줄을 읽어서 공란이나 \n를 제거하고 :을 기준으로 list를 생성
    data = line.strip().split(':')
    kor = data[1];     eng = data[0]
    print(f"{kor}에 대한 영어는 ?")
    answer = input()
    if eng == answer:    print("정답 대박")
    else:    print(f"에효 ! 정당은 {eng}야")
print("종료")
in_file.close()