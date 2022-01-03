jumin = "810120-1068234"
index = jumin.find("-") # 인덱스 위치
print("생년월일 : ",jumin[:index])
print("주민번호 뒷자리 :",jumin[index+1:])