# with와 같이 open하면 auto close된다
with open('test1.txt','w') as f:
    # console이 아니라 파일로 출력
    print('line 1', file=f)
    print('line 2', file=f)
with open('test1.txt','r') as f:
    print(f.read())
