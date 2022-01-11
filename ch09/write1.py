file = open('test.txt','w', encoding='utf-8')
file.write("안녕 컴 동지들 !!\n")
lines = ['안녕하세요',"방가방가","파이썬 대박"]
file.write('\n'.join(lines))
file.close()