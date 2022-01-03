jumin = "810120-1068234"
index = jumin.find("-") # 인덱스 위치
# print(jumin[index+1])
i = jumin[index+1]
if i == '1':
    print('2000년 전 출생한 남자')
elif i == '2':
    print('2000년 전 출생한 여자')
elif i == '3':
    print('2000년 이후 출생한 남자')
elif i == '4':
    print('2000년 이후 출생한 여자')
elif i == '5':
    print('외국인 남자')
elif i == '6':
    print('외국인 여자')
elif i == '7':
    print('외계인')