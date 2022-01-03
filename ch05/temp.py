# 화씨 온도에서 섭씨 온도로 바꿔주는 함수
def fahrenheit_to_celsius(fahrenheit):
    print("화씨 :", fahrenheit)
    c = []
    for i in fahrenheit:
        imsi = (i - 32) * 5 / 9
        c.append(imsi)
    print("섭씨 :",c)

sample_temperature_list = [40, 15, 32, 64, -4, 11]
fahrenheit_to_celsius(sample_temperature_list)

