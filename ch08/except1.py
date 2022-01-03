print("정수를 입력하세요")
num = int(input())
try : 
    print(f"10/{num} : {10/num:.2f}")
except ZeroDivisionError:
    print("0으로 나눌수 없습니다")
except :
    print("에러가 발생했습니다")