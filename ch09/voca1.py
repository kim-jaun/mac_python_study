out_file = open('voca.txt','w',encoding='utf-8')
while True:
    print("영어단어 입력")
    eng = input()
    if eng == 'q':
        break;
    print('한글단어 입력')
    kor = input()
    out_file.write(f"{eng}:{kor}\n")
print("종료")
out_file.close()